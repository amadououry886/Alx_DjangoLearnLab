from django.urls import path
from taggit.models import Tag
from blog.views import search_posts 
from .views import (  # ✅ Import everything from blog.views
    search_posts, register, user_login, user_logout, profile, 
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, 
    add_comment, CommentUpdateView, CommentDeleteView, posts_by_tag, search_posts
)

urlpatterns = [
    # Authentication URLs
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),

    # Blog Post URLs
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # Comment URLs
    path("post/<int:pk>/comments/new/", add_comment, name="comment-create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),

    # Search & Tag URLs
    path("search/", search_posts, name="search_posts"),
    path("tags/<slug:tag_slug>/", posts_by_tag, name="posts_by_tag"),
]
