
from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),  # Ensure exact match
    path("login/", LoginView.as_view(), name="login"),  # Ensure exact match
    path("profile/", ProfileView.as_view(), name="profile"),  # Ensure exact match
]
