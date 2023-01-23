from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
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
