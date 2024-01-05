# Generated by Django 5.0 on 2024-01-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_alter_brokerageasset_operation"),
    ]

    operations = [
        migrations.RenameField(
            model_name="brokerageasset",
            old_name="asset",
            new_name="symbol",
        ),
        migrations.RemoveField(
            model_name="brokerageasset",
            name="balance_in_foreign_currency",
        ),
        migrations.RemoveField(
            model_name="brokerageasset",
            name="balance_in_national_currency",
        ),
        migrations.RemoveField(
            model_name="brokerageasset",
            name="percent_balance_in_foreign_currency",
        ),
        migrations.RemoveField(
            model_name="brokerageasset",
            name="profit",
        ),
        migrations.RemoveField(
            model_name="brokerageasset",
            name="total_balance_in_account",
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="fees",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=10,
                verbose_name="Custos (R$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="for_purchase_exchange_sell",
            field=models.DecimalField(
                decimal_places=4,
                default=0,
                max_digits=10,
                verbose_name="Para compra, câmbio de venda (R$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="for_sale_exchange_purchase",
            field=models.DecimalField(
                decimal_places=4,
                default=0,
                max_digits=10,
                verbose_name="Para venda, câmbio de compra (R$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="origin_in_foreign_currency",
            field=models.DecimalField(
                decimal_places=10,
                default=0,
                max_digits=20,
                verbose_name="Origem moeda estrangeira (US$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="origin_in_national_currency",
            field=models.DecimalField(
                decimal_places=10,
                default=0,
                max_digits=20,
                verbose_name="Origem moeda nacional (US$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="price",
            field=models.DecimalField(
                blank=True,
                decimal_places=10,
                max_digits=20,
                null=True,
                verbose_name="Preço (US$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="purchase_value",
            field=models.DecimalField(
                decimal_places=10,
                default=0,
                max_digits=20,
                verbose_name="Valor da compra (R$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="sell_value",
            field=models.DecimalField(
                decimal_places=10,
                default=0,
                max_digits=20,
                verbose_name="Valor da venda (R$)",
            ),
        ),
        migrations.AlterField(
            model_name="brokerageasset",
            name="total",
            field=models.DecimalField(
                decimal_places=10, max_digits=20, verbose_name="Total (US$)"
            ),
        ),
    ]