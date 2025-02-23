from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app import views  # Import views properly
from .views import list_books

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  #
]
