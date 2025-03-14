from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Book, Author
from rest_framework.test import APITestCase
from rest_framework import status


class BookTestCase(APITestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='testpass')
        self.author1= Author.objects.create(name="aaaa")
        self.author2= Author.objects.create(name="cccc")
        Book.objects.create(title="aa",publication_year=2000,author=self.author1)
        self.client= Client()
        self.client.login(username="testuser", password="testpass") 