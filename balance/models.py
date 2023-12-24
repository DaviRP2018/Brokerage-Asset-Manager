from django.db import models


class Balance(models.Model):
    """Carteira na corretora"""
    national_value = models.FloatField()
    foreign_value = models.FloatField()

    last_addition = models.DateTimeField()


class BalanceIncome(models.Model):
    """Serve para o registro de fluxo de caixa"""
    value = models.FloatField()
    national_fee = models.FloatField()  # IOF + Spread
    exchange_value = models.FloatField()  # Câmbio do dólar
    foreign_fee = models.FloatField()  # Corretagem

    is_dividend = models.BooleanField()
    is_foreign = models.BooleanField()

    history = models.ForeignKey("history.History", on_delete=models.PROTECT)
