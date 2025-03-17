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

    # Blog Post URLs (Updated to match the expected paths)
    path("post/", PostListView.as_view(), name="post-list"),  # View all posts
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),  # View single post
    path("post/new/", PostCreateView.as_view(), name="post-create"),  # Create new post
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  # Edit post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),  # Delete post
]
