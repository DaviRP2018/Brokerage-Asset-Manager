from typing import Iterable

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Avg, Case, F, Sum, When
from django.dispatch import receiver
from django.utils.translation import gettext as _

from positions.models import AccountCashBalance, Order, Positions


# Create your models here.
class BrokerageAsset(models.Model):
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
    )
    origin_in_foreign_currency = models.DecimalField(
        "Origem moeda estrangeira (US$)",
        max_digits=20,
        decimal_places=10,
        default=0,
    )
    for_purchase_exchange_sell = models.DecimalField(
        "Para compra, câmbio de venda (R$)",
        max_digits=10,
        decimal_places=4,
        default=0,
    )
    purchase_value = models.DecimalField(
        "Valor da compra (R$)",
        max_digits=20,
        decimal_places=10,
        default=0,
    )
    for_sale_exchange_purchase = models.DecimalField(
        "Para venda, câmbio de compra (R$)",
        max_digits=10,
        decimal_places=4,
        default=0,
    )
    sell_value = models.DecimalField(
        "Valor da venda (R$)",
        max_digits=20,
        decimal_places=10,
        default=0,
    )

    def save(
        self,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: str | None = ...,
        update_fields: Iterable[str] | None = ...,
    ) -> None:
        national = self.origin_in_national_currency
        foreign = self.origin_in_foreign_currency
        if self.operation in [
            self.DEPOSIT,
            self.SELL,
            self.DIVIDEND,
            self.INTEREST,
        ]:
            # Ensure it's a positive increment
            self.quantity = abs(self.quantity)
            self.total = abs(self.total)
            self.national = abs(national)
            self.foreign = abs(foreign)
        elif self.operation in [self.WITHDRAW, self.BUY]:
            # Ensure it's a negative increment
            self.quantity = -abs(self.quantity)
            self.total = -abs(self.total)
            self.national = -abs(national)
            self.foreign = -abs(foreign)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.date} - {self.symbol}"


@receiver(models.signals.post_save, sender=BrokerageAsset)
def _handle_brokerage_models(sender: BrokerageAsset, **kwargs):
    # Dividend
    foreign_currency = sender.origin_in_foreign_currency
    if sender.operation == sender.DIVIDEND:
        foreign_currency *= 0.70

    # Account balance
    account_cash_balance = AccountCashBalance.objects.first()
    account_cash_balance.balance_in_national_currency += (
        sender.origin_in_national_currency
    )
    account_cash_balance.balance_in_foreign_currency += foreign_currency
    account_cash_balance.total_balance_in_account += sender.total
    account_cash_balance.percent_balance_in_foreign_currency = (
        (
            account_cash_balance.balance_in_foreign_currency
            / account_cash_balance.total_balance_in_account
        )
        if account_cash_balance.total_balance_in_account
        else 0.00
    )
    account_cash_balance.save()

    # Order
    if sender.operation in [sender.BUY, sender.SELL]:
        Order(
            symbol=sender.symbol,
            quantity=sender.quantity,
            value=sender.price,
        ).save()

        # Positions
        orders = Order.objects.filter(symbol=sender.symbol)
        try:
            position = Positions.objects.get(symbol=sender.symbol)
            position.total_quantity = orders.aggregate(Sum("quantity"))
            position.average_value = orders.aggregate(
                Avg(Case(When(quantity__gt=0, then=F("value"))))
            )
            position.save()
        except ObjectDoesNotExist:
            Positions(
                symbol=sender.symbol,
                total_quantity=sender.quantity,
                average_value=sender.price * sender.quantity,
            ).save()

    # History
    # Locally, to avoid circular import
    from history.models import BrokerageHistory

    BrokerageHistory(
        date=sender.date,
        operation=sender.operation,
        symbol=sender.symbol,
        quantity=sender.quantity,
        price=sender.price,
        fees=sender.fees,
        total=sender.total,
        origin_in_national_currency=sender.origin_in_national_currency,
        origin_in_foreign_currency=sender.origin_in_foreign_currency,
        for_purchase_exchange_sell=sender.for_purchase_exchange_sell,
        purchase_value=sender.purchase_value,
        for_sale_exchange_purchase=sender.for_sale_exchange_purchase,
        sell_value=sender.sell_value,
        balance_in_national_currency=account_cash_balance.balance_in_national_currency,  # noqa
        balance_in_foreign_currency=account_cash_balance.balance_in_foreign_currency,  # noqa
        total_balance_in_account=account_cash_balance.total_balance_in_account,
        percent_balance_in_foreign_currency=account_cash_balance.percent_balance_in_foreign_currency,  # noqa
    ).save()
