
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )  # Ensure this is recognized

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "bio", "profile_picture"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )  # Explicitly using `get_user_model().objects.create_user`
        Token.objects.create(user=user)  # Ensure token is created
        return user
