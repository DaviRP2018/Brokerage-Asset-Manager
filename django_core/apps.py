from django.contrib.admin.apps import AdminConfig


class AssetAdminConfig(AdminConfig):
    default_site = "django_core.admin.AssetAdminSite"
