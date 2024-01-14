from django.db import models

from home.models import BrokerageAsset


# Create your models here.
class BrokerageHistory(BrokerageAsset):
    total_balance_in_account = models.DecimalField(
        "Saldo em conta total (US$)", max_digits=10, decimal_places=2
    )
    balance_in_national_currency = models.DecimalField(
        "Saldo moeda nacional (US$)", max_digits=10, decimal_places=2
    )
    balance_in_foreign_currency = models.DecimalField(
        "Saldo moeda estrangeira (US$)", max_digits=10, decimal_places=2
    )
    percent_balance_in_foreign_currency = models.DecimalField(
        "% Saldo em conta moeda estrangeira", max_digits=5, decimal_places=2
    )
