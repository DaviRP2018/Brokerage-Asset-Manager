from django.contrib import admin

from home.forms import BrokerageAssetForm
from home.models import BrokerageAsset


# Register your models here.
class BrokerageAssetAdmin(admin.ModelAdmin):
    form = BrokerageAssetForm
    list_display = [
        "date",
        "operation",
        "symbol",
        "price",
        "total",
    ]
    search_fields = ["symbol"]
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
                    ("symbol", "quantity"),
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
    ]


admin.site.register(BrokerageAsset, BrokerageAssetAdmin)
