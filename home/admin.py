from django.contrib import admin

from home.models import BrokerageAsset


# Register your models here.
class BrokerageAssetAdmin(admin.ModelAdmin):
    list_display = [
        "date",
        "operation",
        "asset",
        "price",
        "total_balance_in_account",
        "percent_balance_in_foreign_currency",
    ]
    search_fields = ["asset"]


admin.site.register(BrokerageAsset, BrokerageAssetAdmin)
admin.AdminSite.site_url = None
