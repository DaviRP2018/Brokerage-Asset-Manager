from django.db import models


class Order(models.Model):
    """Used to be a history of orders, to calculate position"""

    symbol = models.CharField(
        "Ativo",
        max_length=255,
    )
    quantity = models.DecimalField(
        "Quantidade",
        max_digits=20,
        decimal_places=10,
    )
    value = models.DecimalField(
        "Valor (US$)",
        max_digits=20,
        decimal_places=10,
    )
    # fees = models.DecimalField(
    #     "Custos (US$)",
    #     max_digits=10,
    #     decimal_places=2,
    #     default=0,
    # )

    # def save(
    #     self,
    #     force_insert: bool = ...,
    #     force_update: bool = ...,
    #     using: str | None = ...,
    #     update_fields: Iterable[str] | None = ...,
    # ) -> None:
    #     super().save(force_insert, force_update, using, update_fields)
    #     Positions(symbol=self.symbol).save()


class Positions(models.Model):
    """Used to track owned assets"""

    symbol = models.CharField(
        "Ativo",
        max_length=255,
        primary_key=True,
    )
    total_quantity = models.DecimalField(
        "Quantidade",
        max_digits=20,
        decimal_places=10,
    )
    average_value = models.DecimalField(
        "Valor médio (US$)",
        max_digits=20,
        decimal_places=10,
    )
    # profit = models.DecimalField(
    #     "Lucro (R$)",
    #     max_digits=20,
    #     decimal_places=10,
    #     null=True,
    #     blank=True,
    # )

    # def save(
    #     self,
    #     force_insert: bool = ...,
    #     force_update: bool = ...,
    #     using: str | None = ...,
    #     update_fields: Iterable[str] | None = ...,
    # ) -> None:
    #     orders = Order.objects.filter(symbol=self.symbol)
    #     self.total_quantity = orders.aggregate(Sum("quantity"))
    #     self.average_value = orders.aggregate(Avg("value"))
    #     return super().save(force_insert, force_update, using, update_fields)


class AccountCashBalance(models.Model):
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

    def save(self, *args, **kwargs):
        # One account to rule them all
        # For now I will be coding for only one account, to minimize complexity
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        return super().save(*args, **kwargs)
