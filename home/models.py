import decimal
import logging

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Avg, Case, F, Sum, When
from django.dispatch import receiver
from django.utils.translation import gettext as _

from positions.models import AccountCashBalance, Order, Positions


DIVIDEND_TAX = 0.30


# Create your models here.
class BrokerageAbstract(models.Model):
    DEPOSIT = "Deposit"
    WITHDRAW = "Withdraw"
    BUY = "Buy"
    SELL = "Sell"
    DIVIDEND = "Dividend"
    # TODO: Make tax an editable setting, so user can select
    #  if tax is paid or its value
    TAX_PAID = "Tax Paid"
    INTEREST = "Interest"
    OTHER = "Other"

    OPERATION_CHOICES = [
        (DEPOSIT, _("Deposit")),
        (WITHDRAW, _("Withdraw")),
        (BUY, _("Buy")),
        (SELL, _("Sell")),
        (DIVIDEND, _("Dividend")),
        # (TAX_PAID, _("Tax Paid")),
        (INTEREST, _("Interest")),
        (OTHER, _("Other")),
    ]

    date = models.DateField("Data")
    operation = models.CharField(
        "Operação", max_length=20, choices=OPERATION_CHOICES
    )
    symbol = models.CharField(
        "Ativo",
        max_length=255,
        null=True,
        blank=True,
    )
    quantity = models.DecimalField(
        "Quantidade",
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        "Preço (US$)",
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
    )
    fees = models.DecimalField(
        "Custos (R$)",
        max_digits=10,
        decimal_places=2,
        default=0,
        blank=True,
        null=True,
    )
    total = models.DecimalField(
        "Total (US$)",
        max_digits=20,
        decimal_places=10,
    )
    origin_in_national_currency = models.DecimalField(
        "Origem moeda nacional (US$)",
        max_digits=20,
        decimal_places=10,
        default=0,
        blank=True,
        null=True,
    )
    origin_in_foreign_currency = models.DecimalField(
        "Origem moeda estrangeira (US$)",
        max_digits=20,
        decimal_places=10,
        default=0,
        blank=True,
        null=True,
    )
    for_purchase_exchange_sell = models.DecimalField(
        "Para compra, câmbio de venda (R$)",
        max_digits=10,
        decimal_places=4,
        default=0,
        blank=True,
        null=True,
    )
    purchase_value = models.DecimalField(
        "Valor da compra (R$)",
        max_digits=20,
        decimal_places=10,
        default=0,
        blank=True,
        null=True,
    )
    for_sale_exchange_purchase = models.DecimalField(
        "Para venda, câmbio de compra (R$)",
        max_digits=10,
        decimal_places=4,
        default=0,
        blank=True,
        null=True,
    )
    sell_value = models.DecimalField(
        "Valor da venda (R$)",
        max_digits=20,
        decimal_places=10,
        default=0,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.date} - {self.symbol}"


class BrokerageAsset(BrokerageAbstract):
    def save(self, *args, **kwargs):
        national = self.origin_in_national_currency
        foreign = self.origin_in_foreign_currency
        if self.operation in [
            self.DEPOSIT,
            self.SELL,
            self.DIVIDEND,
            self.INTEREST,
        ]:
            # Ensure it's a positive increment
            self.total = abs(self.total)
            self.quantity = -abs(self.quantity) if self.quantity else 0
            if self.operation == self.SELL:
                # Percentage
                acc_balance = AccountCashBalance.objects.first()
                acc_percent = acc_balance.percent_balance_in_foreign_currency
                self.origin_in_foreign_currency = acc_percent * self.total
                self.origin_in_national_currency = (
                    1 - acc_percent
                ) * self.total
            else:
                self.origin_in_national_currency = (
                    abs(national) if national else 0
                )
                self.origin_in_foreign_currency = (
                    abs(foreign) if foreign else 0
                )
        elif self.operation in [self.WITHDRAW, self.BUY]:
            # Ensure it's a negative increment
            self.total = -abs(self.total)
            self.quantity = abs(self.quantity) if self.quantity else 0
            self.origin_in_national_currency = (
                -abs(national) if national else 0
            )
            self.origin_in_foreign_currency = -abs(foreign) if foreign else 0
            # Percentage
            acc_balance = AccountCashBalance.objects.first()
            acc_percent = acc_balance.percent_balance_in_foreign_currency
            self.origin_in_foreign_currency = acc_percent * self.total
            self.origin_in_national_currency = (1 - acc_percent) * self.total
        return super().save(*args, **kwargs)


@receiver(models.signals.post_save, sender=BrokerageAsset)
def _handle_brokerage_models(sender, **kwargs):
    instance = kwargs["instance"]
    logger = logging.getLogger("_handle_brokerage_models")

    # Dividend
    foreign_currency = instance.origin_in_foreign_currency
    total = instance.total
    logger.debug("foreign_currency: %s", foreign_currency)

    if instance.operation == instance.DIVIDEND:
        foreign_currency *= 1 - DIVIDEND_TAX
        total *= 1 - DIVIDEND_TAX

    # Account balance
    acc_balance = AccountCashBalance.objects.first()
    acc_balance.balance_in_national_currency = (
        acc_balance.balance_in_national_currency
        + instance.origin_in_national_currency
    )
    acc_balance.balance_in_foreign_currency = (
        acc_balance.balance_in_foreign_currency
        + decimal.Decimal(foreign_currency)
    )
    acc_balance.total_balance_in_account = (
        acc_balance.total_balance_in_account + decimal.Decimal(total)
    )
    acc_balance.percent_balance_in_foreign_currency = (
        (
            acc_balance.balance_in_foreign_currency
            / acc_balance.total_balance_in_account
        )
        if acc_balance.total_balance_in_account
        else 0.00
    )
    acc_balance.save()

    # Order
    if instance.operation in [instance.BUY, instance.SELL]:
        Order(
            symbol=instance.symbol,
            quantity=instance.quantity,
            value=instance.price,
        ).save()

        # Positions
        orders = Order.objects.filter(symbol=instance.symbol)
        try:
            position = Positions.objects.get(symbol=instance.symbol)
            position.total_quantity = orders.aggregate(Sum("quantity"))[
                "quantity__sum"
            ]
            position.average_value = orders.aggregate(
                value__avg=Avg(Case(When(quantity__gt=0, then=F("value"))))
            )["value__avg"]
            position.save()
        except ObjectDoesNotExist:
            Positions(
                symbol=instance.symbol,
                total_quantity=instance.quantity,
                average_value=instance.price * instance.quantity,
            ).save()

    # History
    # Locally, to avoid circular import
    from history.models import BrokerageHistory

    BrokerageHistory(
        date=instance.date,
        operation=instance.operation,
        symbol=instance.symbol,
        quantity=instance.quantity,
        price=instance.price,
        fees=instance.fees,
        total=total,
        origin_in_national_currency=instance.origin_in_national_currency,
        origin_in_foreign_currency=instance.origin_in_foreign_currency,
        for_purchase_exchange_sell=instance.for_purchase_exchange_sell,
        purchase_value=instance.purchase_value,
        for_sale_exchange_purchase=instance.for_sale_exchange_purchase,
        sell_value=instance.sell_value,
        balance_in_national_currency=acc_balance.balance_in_national_currency,  # noqa
        balance_in_foreign_currency=acc_balance.balance_in_foreign_currency,  # noqa
        total_balance_in_account=acc_balance.total_balance_in_account,
        percent_balance_in_foreign_currency=acc_balance.percent_balance_in_foreign_currency,  # noqa
    ).save()
    if instance.operation == instance.DIVIDEND:
        BrokerageHistory(
            date=instance.date,
            operation=instance.TAX_PAID,
            symbol=instance.symbol,
            quantity=instance.quantity,
            price=instance.price,
            fees=instance.fees,
            total=instance.total * DIVIDEND_TAX,
            origin_in_national_currency=instance.origin_in_national_currency,
            origin_in_foreign_currency=instance.origin_in_foreign_currency,
            for_purchase_exchange_sell=instance.for_purchase_exchange_sell,
            purchase_value=instance.purchase_value,
            for_sale_exchange_purchase=instance.for_sale_exchange_purchase,
            sell_value=instance.sell_value,
            balance_in_national_currency=acc_balance.balance_in_national_currency,  # noqa
            balance_in_foreign_currency=acc_balance.balance_in_foreign_currency,  # noqa
            total_balance_in_account=acc_balance.total_balance_in_account,
            percent_balance_in_foreign_currency=acc_balance.percent_balance_in_foreign_currency,  # noqa
        ).save()
