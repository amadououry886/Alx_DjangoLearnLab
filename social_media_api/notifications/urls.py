from django.urls import path
from posts.views import get_notifications

urlpatterns = [
    path('', get_notifications, name='notifications'),
]
