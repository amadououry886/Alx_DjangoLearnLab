
from django.urls import path
from accounts.views import RegisterView, LoginView, ProfileView  # Explicit relative import
from .views import FollowUserView, UnfollowUserView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),  # Explicit path match
    path("login/", LoginView.as_view(), name="login"),  # Explicit path match
    path("profile/", ProfileView.as_view(), name="profile"),  # Explicit path match
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),

]
