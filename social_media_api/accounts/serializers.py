from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "bio", "profile_picture"]

    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # <- REQUIRED
        Token.objects.create(user=user)  # <- REQUIRED
        return user