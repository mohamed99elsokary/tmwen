from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register),
    path("login/", views.login),
    path("profile/", views.profile),
    # cart
    path("cart/", views.cart),
    path("cart-details/", views.cart_details),
    path("cart-product/", views.delete_product_from_cart),
]
