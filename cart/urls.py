from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path("", views.cartPage, name="cart"),
    path("add", views.addCart, name="addCart"),
]
