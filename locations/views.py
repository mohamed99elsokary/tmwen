from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers


@api_view(["GET"])
def country(request):
    countries = models.Country.objects.all()
    serializer = serializers.CountrySerializer(countries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def country_cities(request, id):
    country = get_object_or_404(models.Country, id=id)
    cities = get_list_or_404(models.City, country=country)
    serializer = serializers.CitySerializer(cities, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
