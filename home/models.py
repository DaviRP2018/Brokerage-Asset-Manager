from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class BrokerageAsset(models.Model):
    DEPOSIT = "Deposit"
    BUY = "Buy"
    SELL = "Sell"
    DIVIDEND = "Dividend"
    TAX_PAID = "Tax Paid"
    INTEREST = "Interest"
    OTHER = "Other"

    OPERATION_CHOICES = [
        (DEPOSIT, _("Deposit")),
        (BUY, _("Buy")),
        (SELL, _("Sell")),
        (DIVIDEND, _("Dividend")),
        (TAX_PAID, _("Tax Paid")),
        (INTEREST, _("Interest")),
        (OTHER, _("Other")),
    ]

    date = models.DateField()
    operation = models.CharField(max_length=20, choices=OPERATION_CHOICES)
    asset = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=20, decimal_places=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    costs = models.DecimalField(max_digits=10, decimal_places=2)
    total_in_usd = models.DecimalField(max_digits=10, decimal_places=2)
    origin_in_national_currency = models.CharField(max_length=255)
    origin_in_foreign_currency = models.CharField(max_length=255)
    for_purchase_exchange_sell = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    for_sale_exchange_purchase = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    profit_in_r = models.DecimalField(max_digits=10, decimal_places=2)
    balance_in_national_currency = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    balance_in_foreign_currency = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    total_balance_in_account = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    percent_balance_in_foreign_currency = models.DecimalField(
        max_digits=5, decimal_places=2
    )

    def __str__(self):
        return f"{self.date} - {self.asset}"
