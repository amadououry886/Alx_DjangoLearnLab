from django.urls import path
from .views import list_books, LibraryDetailView
from django.urls import path
from .views import register, user_login, user_logout
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/', list_books, name='list_books'),  # FBV for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV for library details
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
]
