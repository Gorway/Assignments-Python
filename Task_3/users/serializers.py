from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username"]


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["email", "password"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data["email"],
            username=validated_data["email"],
            password=validated_data["password"],
        )
        return user
