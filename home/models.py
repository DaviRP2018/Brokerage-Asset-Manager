from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class BrokerageAsset(models.Model):
    DEPOSIT = "Deposit"
    WITHDRAW = "Withdraw"
    BUY = "Buy"
    SELL = "Sell"
    DIVIDEND = "Dividend"
    TAX_PAID = "Tax Paid"
    INTEREST = "Interest"
    OTHER = "Other"

    OPERATION_CHOICES = [
        (DEPOSIT, _("Deposit")),
        (WITHDRAW, _("Withdraw")),
        (BUY, _("Buy")),
        (SELL, _("Sell")),
        (DIVIDEND, _("Dividend")),
        (TAX_PAID, _("Tax Paid")),
        (INTEREST, _("Interest")),
        (OTHER, _("Other")),
    ]

    date = models.DateField("Data")
    operation = models.CharField(
        "Operação", max_length=20, choices=OPERATION_CHOICES
    )
    asset = models.CharField(
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
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    fees = models.DecimalField(
        "Custos (R$)",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    total = models.DecimalField("Total (US$)", max_digits=10, decimal_places=2)
    origin_in_national_currency = models.CharField(
        "Origem moeda nacional (US$)",
        max_length=255,
        null=True,
        blank=True,
    )
    origin_in_foreign_currency = models.CharField(
        "Origem moeda estrangeira (US$)",
        max_length=255,
        null=True,
        blank=True,
    )
    for_purchase_exchange_sell = models.DecimalField(
        "Para compra, câmbio de venda (R$)",
        max_digits=10,
        decimal_places=4,
        null=True,
        blank=True,
    )
    purchase_value = models.DecimalField(
        "Valor da compra (R$)",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    for_sale_exchange_purchase = models.DecimalField(
        "Para venda, câmbio de compra (R$)",
        max_digits=10,
        decimal_places=4,
        null=True,
        blank=True,
    )
    sell_value = models.DecimalField(
        "Valor da venda (R$)",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    profit = models.DecimalField(
        "Lucro (R$)",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    balance_in_national_currency = models.DecimalField(
        "Saldo moeda nacional (US$)", max_digits=10, decimal_places=2
    )
    balance_in_foreign_currency = models.DecimalField(
        "Saldo moeda estrangeira (US$)", max_digits=10, decimal_places=2
    )
    total_balance_in_account = models.DecimalField(
        "Saldo em conta total (US$)", max_digits=10, decimal_places=2
    )
    percent_balance_in_foreign_currency = models.DecimalField(
        "% Saldo em conta moeda estrangeira", max_digits=5, decimal_places=2
    )

    def __str__(self):
        return f"{self.date} - {self.asset}"
