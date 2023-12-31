from django.contrib import admin

from home.forms import BrokerageAssetForm
from home.models import BrokerageAsset


# Register your models here.
class BrokerageAssetAdmin(admin.ModelAdmin):
    form = BrokerageAssetForm
    list_display = [
        "date",
        "operation",
        "asset",
        "price",
        "total_balance_in_account",
        "percent_balance_in_foreign_currency",
    ]
    search_fields = ["asset"]
    readonly_fields = [
        "profit",
        "balance_in_national_currency",
        "balance_in_foreign_currency",
        "total_balance_in_account",
        "percent_balance_in_foreign_currency",
    ]
    fieldsets = [
        (
            None,
            {
                "fields": ["date", "operation"],
            },
        ),
        (
            "Dynamic",
            {
                "classes": ["brokerage-dynamic-field"],
                "fields": [
                    ("asset", "quantity"),
                    "price",
                    "fees",
                    "total",
                    (
                        "origin_in_national_currency",
                        "origin_in_foreign_currency",
                    ),
                    ("for_purchase_exchange_sell", "purchase_value"),
                    ("for_sale_exchange_purchase", "sell_value"),
                ],
            },
        ),
        (
            "Result",
            {
                "fields": [
                    "profit",
                    (
                        "balance_in_national_currency",
                        "balance_in_foreign_currency",
                        "total_balance_in_account",
                    ),
                    "percent_balance_in_foreign_currency",
                ]
            },
        ),
    ]


admin.site.register(BrokerageAsset, BrokerageAssetAdmin)
