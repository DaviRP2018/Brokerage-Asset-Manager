from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class BrokerageAsset(models.Model):
    DEPOSIT = "Deposit"
    WITHDRAW = "Withdraw"
    BUY = "Buy"
    SELL = "Sell"
    DIVIDEND = "Dividend"
    # TODO: Make tax be a editable setting
    # TAX_PAID = "Tax Paid"
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

    def __str__(self):
        return f"{self.date} - {self.symbol}"
