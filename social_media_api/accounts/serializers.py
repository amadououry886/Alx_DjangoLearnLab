
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])  # ✅ Ensure serializers.CharField()
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 before saving
        user = User.objects.create_user(**validated_data)  # ✅ Explicitly use get_user_model().objects.create_user
        Token.objects.create(user=user)  # Create auth token for the user
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)  # ✅ Ensure serializers.CharField()
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        return {'user': user, 'token': Token.objects.get_or_create(user=user)[0].key}

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']
