from django.urls import path
from . import views

urlpatterns = [
    path("vendors/", views.vendors),
    path("vendor/<slug:id>", views.vendor_details),
    path("vendor/products/<int:id>", views.vendor_products),
    path("vendor/product/<int:id>", views.product_details),
]
