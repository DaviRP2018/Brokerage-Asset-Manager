# Generated by Django 5.0 on 2023-12-27 01:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_alter_brokerageasset_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brokerageasset",
            name="operation",
            field=models.CharField(
                choices=[
                    ("Deposit", "Deposit"),
                    ("Withdraw", "Withdraw"),
                    ("Buy", "Buy"),
                    ("Sell", "Sell"),
                    ("Dividend", "Dividend"),
                    ("Tax Paid", "Tax Paid"),
                    ("Interest", "Interest"),
                    ("Other", "Other"),
                ],
                max_length=20,
                verbose_name="Operação",
            ),
        ),
    ]