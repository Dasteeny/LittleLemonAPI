from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Cart, Category, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            "id",
            "title",
            "price",
            "featured",
            "category",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
        extra_kwargs = {"email": {"read_only": True}}


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "id",
            "menuitem",
            "quantity",
            "unit_price",
            "price",
        ]
        extra_kwargs = {
            "quantity": {"min_value": 1},
            "unit_price": {"read_only": True},
            "price": {"read_only": True},
            "menuitem": {"label": "Menu Item"},
        }
