from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from accounts.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import CustomUser

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
    
api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    request.user.follow(user_to_follow)
    return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    request.user.unfollow(user_to_unfollow)
    return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)