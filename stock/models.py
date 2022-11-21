from django.db import models


# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=255)
    action = models.CharField(max_length=255,
                              choices={
                                  "buy": "Buy",
                                  "sell": "Sell"
                              })

    