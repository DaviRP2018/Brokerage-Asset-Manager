from django.db import models


class Stock(models.Model):
    """Carteira de papéis"""
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    live_foreign_value = models.FloatField()
    value = models.FloatField()

    average_buy_price = models.FloatField()


class StockIncome(models.Model):
    """Serve para o registro do fluxo de stocks"""
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    foreign_value = models.FloatField()  # preço
    foreign_fee = models.FloatField()  # custos
    exchange_value = models.FloatField()  # dólar na compra

    history = models.ForeignKey("History", on_delete=models.PROTECT)
