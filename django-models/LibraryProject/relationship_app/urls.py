from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app import views  # Import views properly
from .views import list_books
from .views import register
from .admin_view import admin_dashboard
from .librarian_view import librarian_dashboard
from .member_view import member_dashboard
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  #
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout view

    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
]
