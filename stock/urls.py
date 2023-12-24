from django.urls import path

from . import views

urlpatterns = [
    path("/stocks", views.index, name="index")
]
