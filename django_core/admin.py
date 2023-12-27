from django.contrib import admin


admin.AdminSite.site_url = None


class AssetAdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context["test"] = "test_"
        return super().index(request, extra_context)
