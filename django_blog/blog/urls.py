from django.urls import path
from .views import (
    register, user_login, user_logout, profile, 
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    # Authentication URLs
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),

    # Blog Post URLs
    path("posts/", PostListView.as_view(), name="post-list"),  # View all posts
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),  # View single post
    path("posts/new/", PostCreateView.as_view(), name="post-create"),  # Create new post
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),  # Edit post
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),  # Delete post
]
