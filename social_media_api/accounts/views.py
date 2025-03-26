from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from accounts.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserSerializer

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)  # ✅ Use UserRegistrationSerializer
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)  # ✅ Ensure token creation
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)  # ✅ Use UserLoginSerializer
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)  # ✅ Return validated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    def get(self, request):
        serializer = UserProfileSerializer(request.user)  # ✅ Use UserProfileSerializer
        return Response(serializer.data)
