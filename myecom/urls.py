from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.staticfiles.views import serve


urlpatterns = [
    path("admin/", admin.site.urls),
    path("products", include("products.urls")),
    path("cart/", include("cart.urls")),
    path("checkout/", include("checkout.urls")),
    path("", include("homepage.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("/<path:path>", serve, {"document_root": settings.STATIC_URL}),
]
