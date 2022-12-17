from django.db import models


class IRBaseSettings(models.Model):
    """Configurações do quanto é cobrado"""
    fee = models.FloatField()
    is_percentage = models.BooleanField()


class IRDividendSettings(IRBaseSettings):
    """Configurações para os proventos"""
    fee_type = models.CharField(max_length=255, default="Provento")


class IR(models.Model):
    """Controle de impostos pagos ou não"""
    history = models.ForeignKey("History", on_delete=models.PROTECT)

    value = models.FloatField()
    paid = models.BooleanField()

    due_date = models.DateField()
