from django.urls import path
from . import views

urlpatterns = [
    path("country/", views.country),
    path("country/<int:id>/", views.country_cities),
]
