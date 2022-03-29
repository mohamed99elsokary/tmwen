from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models
from django.shortcuts import get_object_or_404


class VendorSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(read_only=True, slug_field="country")
    city = serializers.SlugRelatedField(read_only=True, slug_field="city")

    class Meta:
        model = models.Vendor
        fields = "__all__"


class Products(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    token = serializers.CharField(write_only=True)

    class Meta:
        model = models.Product
        fields = "__all__"

    def create(self, data):
        user = get_object_or_404(Token, key=data.get("token")).user
        vendor = get_object_or_404(models.Vendor, user=user)
        data["vendor"] = vendor
        data.pop("token")
        product = models.Product.objects.create(**data)
        return product
