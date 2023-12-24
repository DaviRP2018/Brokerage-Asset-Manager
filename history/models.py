from django.db import models


class History(models.Model):
    """Historico e registro de toda transação"""

    entry_type = models.CharField(max_length=255)

    national_balance_value_before = models.FloatField()
    national_balance_value_after = models.FloatField()

    foreign_balance_value_before = models.FloatField()
    foreign_balance_value_after = models.FloatField()

    total_balance_value_before = models.FloatField()
    total_balance_value_after = models.FloatField()

    date = models.DateField()
    time = models.TimeField()
