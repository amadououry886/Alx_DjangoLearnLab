from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app import views  # Import views properly
from .views import list_books
from .views import register
from django.urls import path
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view
from django.contrib.auth.views import LoginView, LogoutView
# from .models import LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    # path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  #
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout view

    path('admin/',views. admin_view, name='admin_dashboard'),
    path('librarian/', views.librarian_view, name='librarian_dashboard'),
    path('member/', views.member_view, name='member_dashboard'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
]
