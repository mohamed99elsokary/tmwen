from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from profiles import models as profiles
from . import models, serializers


@api_view(["POST"])
def vendors(request):
    if request.data.get("city"):
        vendors = models.Vendor.objects.filter(city_id=request.data.get("city"))
    elif request.data.get("token"):
        user = get_object_or_404(Token, key=request.data("token")).user
        country = get_object_or_404(profiles.Profile, user=user).country
        vendors = models.Vendor.objects.filter(country=country)
    else:
        vendors = models.Vendor.objects.all()

    serializer = serializers.VendorSerializer(vendors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT", "POST", "GET"])
def vendor_details(request, id):
    if request.method == "GET":
        print(id)
        user = get_object_or_404(Token, key=id).user
        vendor = get_object_or_404(models.Vendor, user=user)
        serializer = serializers.VendorSerializer(vendor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        user = get_object_or_404(Token, key=id).user
        vendor = get_object_or_404(models.Vendor, user=user)
        if request.data.get("country") not in ["None", ""]:
            vendor.country_id = request.data.get("country")
        if request.data.get("city") not in ["None", ""]:
            vendor.city_id = request.data.get("city")
        if request.data.get("name") not in ["None", ""]:
            vendor.name = request.data.get("name")
        if request.data.get("LAT") not in ["None", ""]:
            vendor.LAT = request.data.get("LAT")
        if request.data.get("LONG") not in ["None", ""]:
            vendor.LONG = request.data.get("LONG")
        if request.data.get("address") not in ["None", ""]:
            vendor.address = request.data.get("address")
        if request.data.get("open_time") not in ["None", ""]:
            vendor.open_time = request.data.get("open_time")
        if request.data.get("close_time") not in ["None", ""]:
            vendor.close_time = request.data.get("close_time")
        vendor.save()
        serializer = serializers.VendorSerializer(vendor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        user = get_object_or_404(Token, key=request.data.get("token")).user
        vendor = get_object_or_404(models.Vendor, user=user)
        vendor.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["POST", "GET"])
def vendor_products(request, id):
    if request.method == "GET":
        vendor = get_object_or_404(models.Vendor, id=id)
        products = get_list_or_404(models.Product, vendor=vendor)
        serializer = serializers.ProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = serializers.ProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT", "DELETE", "GET"])
def product_details(request, id):
    if request.method == "GET":
        product = get_object_or_404(models.Product, id=id)
        serializer = serializers.ProductsSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":

        product = get_object_or_404(models.Product, id=id).delete()
        return Response(status=status.HTTP_200_OK)
    if request.method == "PUT":
        user = get_object_or_404(Token, key=request.data.get("token")).user
        vendor = get_object_or_404(models.Vendor, user=user)
        product = get_object_or_404(models.Product, id=id)
        if product.vendor != vendor:
            return Response("Invalid Vendor Item", status=status.HTTP_400_BAD_REQUEST)
        if request.data.get("name") not in ["None", ""]:
            product.name = request.data.get("name")
        if request.data.get("price") not in ["None", ""]:
            product.price = request.data.get("price")
        if request.data.get("quantity") not in ["None", ""]:
            product.quantity = request.data.get("quantity")
        product.save()
        serializer = serializers.ProductsSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
