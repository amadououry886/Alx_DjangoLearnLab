
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )  # Explicit CharField

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "bio", "profile_picture"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )  # Ensure explicit field usage
        Token.objects.create(user=user)  # Token creation
        return user
