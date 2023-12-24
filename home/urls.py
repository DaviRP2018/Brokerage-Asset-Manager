from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("add-item/", views.AddItemView.as_view(), name="add_item"),
]
