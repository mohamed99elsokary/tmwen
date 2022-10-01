from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from locations import models as locations
from vendors import serializers as vendors_serializers
from . import models


class RegisterUserSerializer(serializers.ModelSerializer):
    token = serializers.SlugRelatedField(
        read_only=True, source="auth_token", slug_field="key"
    )

    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    country = serializers.IntegerField(write_only=True)
    city = serializers.IntegerField(write_only=True)
    credit = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "token",
            "password",
            "email",
            "first_name",
            "last_name",
            "country",
            "city",
            "credit",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"write_only": True},
            "email": {"write_only": True},
        }

    def validate(self, data):
        if len(data["password"]) < 8:
            raise serializers.ValidationError(
                {"password": "password must to be more than 7 or more characters"}
            )
        if data.get("email") == "":
            raise serializers.ValidationError({"email": "email can't be empty"})
        if not (data.get("email")):
            raise serializers.ValidationError({"email": "email is required"})
        get_object_or_404(
            locations.City,
            id=data["city"],
        )
        get_object_or_404(
            locations.Country,
            id=data["country"],
        )
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(password)
        user.save()
        token = Token(user=user)
        token.save()
        profile = models.Profile(
            user=user,
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            credit=validated_data["credit"],
            country_id=validated_data["country"],
            city_id=validated_data["city"],
        )
        profile.save()
        return user


class LoginUserSerializer(serializers.ModelSerializer):
    token = serializers.SlugRelatedField(
        read_only=True, source="auth_token", slug_field="key"
    )

    class Meta:
        model = User
        fields = ["username", "token", "password", "email"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"write_only": True},
            "username": {"validators": [], "write_only": True},
        }

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user is None:
            raise serializers.ValidationError(
                {"error": "Invalid Username And Password"}
            )
        else:
            return user


class ProfileSerializer(serializers.ModelSerializer):
    token = serializers.IntegerField(write_only=True)
    country = serializers.SlugRelatedField(read_only=True, slug_field="country")
    city = serializers.SlugRelatedField(read_only=True, slug_field="city")

    class Meta:
        model = models.Profile
        exclude = ("user",)


class CartSerializer(serializers.ModelSerializer):
    vendor = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # product = serializers.SlugRelatedField(slug_field="name", read_only=True)
    product = vendors_serializers.Products(
        many=False,
        read_only=True,
    )

    class Meta:
        model = models.Cart
        fields = "__all__"
