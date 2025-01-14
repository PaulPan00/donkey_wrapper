"""
Allows data/models to be converted to python datatypes and then easily rendered into JSON\

manages what gets return from the api

"""

from blog.models import Post
from django.conf import settings
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

        # data to manage
        fields = (
            "category",
            "id",
            "title",
            "image",
            "slug",
            "author",
            "excerpt",
            "content",
            "status",
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ("email", "user_name", "first_name")
        extra_kwargs = {"password": {"write_only": True}}
