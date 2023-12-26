from django.contrib import admin


class AssetAdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context["test"] = "test_"
        return super().index(request, extra_context)
