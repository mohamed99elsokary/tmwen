from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from . import serializers, models
from vendors import models as vendors
from django.contrib.auth.models import User

# Create your views here.
@api_view(["POST"])
def register(request):
    serializer = serializers.RegisterUserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@csrf_exempt
def login(request):
    user = User.objects.get(username=request.data.get("username"))
    try:
        profile = models.Profile.objects.get(user=user)
        user_type = 1
        vendor_id = None
    except:
        pass
    try:
        vendor = vendors.Vendor.objects.get(user=user)
        vendor_id = vendor.id
        user_type = 2
    except:
        pass

    serializer = serializers.LoginUserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
        data["user_type"] = user_type
        data["vendor_id"] = vendor_id
        return Response(data, status=status.HTTP_200_OK)


@api_view(["POST", "PUT", "DELETE"])
def profile(request):
    user = get_object_or_404(Token, key=request.data["token"]).user
    profile = get_object_or_404(models.Profile, user=user)
    # get profile data
    if request.method == "POST":
        serializer = serializers.ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # update profile data
    elif request.method == "PUT":
        if request.data.get("country") != None and request.data.get("country") != "":
            profile.country_id = request.data.get("country")
        if request.data.get("city") != None and request.data.get("city") != "":
            profile.city_id = request.data.get("city")
        if (
            request.data.get("first_name") != None
            and request.data.get("first_name") != ""
        ):
            profile.first_name = request.data.get("first_name")
        if (
            request.data.get("last_name") != None
            and request.data.get("last_name") != ""
        ):
            profile.last_name = request.data.get("last_name")
        if request.data.get("credit") != None and request.data.get("credit") != "":
            profile.credit = request.data.get("credit")

        profile.save()
        serializer = serializers.ProfileSerializer(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # delete profile and user
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_200_OK)


# cart
@api_view(["POST", "PUT"])
def cart_details(request):
    if request.method == "POST":
        user = get_object_or_404(Token, key=request.data.get("token")).user
        product = get_object_or_404(vendors.Product, id=request.data.get("product"))
        cart = models.Cart.objects.create(
            user=user,
            vendor=product.vendor,
            product=product,
            quantity=request.data.get("quantity"),
        )
        serializer = serializers.CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        user = get_object_or_404(Token, key=request.data.get("token")).user
        product = get_object_or_404(models.Cart, id=request.data.get("id"), user=user)
        if request.data.get("quantity") != None and request.data.get("quantity") != "":
            product.quantity = request.data.get("quantity")
            product.save()
        serializer = serializers.CartSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def delete_product_from_cart(request):
    if request.method == "POST":
        user = get_object_or_404(Token, key=request.data.get("token")).user
        product = get_object_or_404(
            models.Cart, id=request.data.get("id"), user=user
        ).delete()
        return Response(status=status.HTTP_200_OK)


# get cart items
@api_view(["POST"])
def cart(request):
    if request.method == "POST":
        user = get_object_or_404(Token, key=request.data.get("token")).user
        cart = models.Cart.objects.filter(user=user)
        serializer = serializers.CartSerializer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
