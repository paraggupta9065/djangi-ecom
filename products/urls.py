from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path("/add/", views.addProduct, name="addProduct"),
    path("/category/add/", views.addCategory, name="addCategory"),
    path("/get/", views.addCategory, name="addCategory"),
    path("/", views.viewProducts, name="viewProducts"),
    path("/view/", views.viewProduct, name="viewProduct"),
]
