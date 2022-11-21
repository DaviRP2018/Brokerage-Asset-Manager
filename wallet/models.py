from django.db import models


# Create your models here.
class Wallet(models.Model):
    national_value = models.FloatField()
    foreign_value = models.FloatField()

    last_addition = models.DateTimeField()


class WalletAdd(models.Model):
    value = models.FloatField()
    national_fee = models.FloatField()
    foreign_fee = models.FloatField()
    exchange_value = models.FloatField()

    is_dividend = models.BooleanField()
    is_foreign = models.BooleanField()

    date = models.DateField()
    time = models.TimeField()
