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
                ]
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
                    ),
                    "total_balance_in_account",
                    "percent_balance_in_foreign_currency",
                ]
            },
        ),
        # (
        #     "Deposit",
        #     {
        #         "classes": ["collapse"],
        #         "fields": [
        #             "fees",
        #             "total",
        #             "origin_in_national_currency",
        #             "origin_in_foreign_currency",
        #             "for_purchase_exchange_sell",
        #             "purchase_value",
        #         ]
        #     }
        # ),
        # (
        #     "Withdraw",
        #     {
        #         "classes": ["collapse"],
        #         "fields": [
        #             "fees",
        #             "total",
        #             "origin_in_national_currency",
        #             "origin_in_foreign_currency",
        #             "for_sale_exchange_purchase",
        #             "sell_value",
        #         ]
        #     }
        # ),
        # (
        #     "Buy",
        #     {
        #         "classes": ["collapse"],
        #         "fields": [
        #             "asset",
        #             "quantity",
        #             "price",
        #             "total",
        #             "origin_in_national_currency",
        #             "origin_in_foreign_currency",
        #             "for_purchase_exchange_sell",
        #             "purchase_value",
        #         ]
        #     }
        # ),
        # (
        #     "Sell",
        #     {
        #         "classes": ["collapse"],
        #         "fields": [
        #             "asset",
        #             "quantity",
        #             "price",
        #             "total",
        #             "origin_in_national_currency",
        #             "origin_in_foreign_currency",
        #             "for_sale_exchange_purchase",
        #             "sell_value",
        #         ]
        #     }
        # ),
        # (
        #     "Dividend",
        #     {
        #         "classes": ["collapse"],
        #         "fields": [
        #             "asset",
        #             "total",
        #             "origin_in_foreign_currency",
        #             "for_sale_exchange_purchase",
        #             "sell_value",
        #         ]
        #     }
        # ),
        # (
        #     "Tax Paid",
        #     {
        #         "classes": ["collapse"],
        #         "fields": [
        #             "asset",
        #             "total",
        #             "origin_in_foreign_currency",
        #             "for_sale_exchange_purchase",
        #             "sell_value",
        #         ]
        #     }
        # ),
        # (
        #     "Interest",
        #     {
        #         "classes": ["collapse"],
        #         "fields": [
        #             "total",
        #             "origin_in_foreign_currency",
        #         ]
        #     }
        # ),
        # (
        #     "Other",
        #     {
        #         "classes": ["collapse"],
        #         "fields": [
        #             "asset",
        #             "quantity",
        #             "price",
        #             "fees",
        #             "total",
        #             "origin_in_national_currency",
        #             "origin_in_foreign_currency",
        #             "for_purchase_exchange_sell",
        #             "purchase_value",
        #             "for_sale_exchange_purchase",
        #             "sell_value",
        #         ]
        #     }
        # ),
    ]


admin.site.register(BrokerageAsset, BrokerageAssetAdmin)
