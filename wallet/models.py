from django.db import models


class Wallet(models.Model):
    """Carteira na corretora"""
    national_value = models.FloatField()
    foreign_value = models.FloatField()

    last_addition = models.DateTimeField()


class WalletIncome(models.Model):
    """Serve para o registro de fluxo de caixa"""
    value = models.FloatField()
    national_fee = models.FloatField()
    foreign_fee = models.FloatField()
    exchange_value = models.FloatField()

    is_dividend = models.BooleanField()
    is_foreign = models.BooleanField()

    date = models.DateField()
    time = models.TimeField()
