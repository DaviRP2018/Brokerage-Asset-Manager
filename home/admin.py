from django.contrib import admin

from home.models import BrokerageAsset


# Register your models here.
class BrokerageAssetAdmin(admin.ModelAdmin):
    pass


admin.site.register(BrokerageAsset, BrokerageAssetAdmin)
