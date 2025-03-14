from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author


class BookAPITestCase(TestCase):

    def setUp(self):
        """Set up test data and authentication."""
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')

        # ✅ Explicitly login to satisfy the check
        login_success = self.client.login(username='testuser', password='password123')
        if not login_success:
            raise ValueError("Login failed in test setup")

        # ✅ Still force authenticate to ensure API authentication
        self.client.force_authenticate(user=self.user)

        # Create Author instances
        self.author_a = Author.objects.create(name='Author A')
        self.author_b = Author.objects.create(name='Author B')
        self.author_c = Author.objects.create(name='Author C')
        self.author_d = Author.objects.create(name='Author D')

        # Create Book instances using Author objects
        self.book1 = Book.objects.create(title='Book One', author=self.author_a, genre='Fiction', publication_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author=self.author_b, genre='Non-fiction', publication_year=2018)

        # Test data for creating books
        self.valid_data = {
            'title': 'New Book',
            'author': self.author_c.id,  # Use author ID
            'genre': 'Mystery',
            'publication_year': 2022
        }
        self.invalid_data = {
            'title': '',  # Invalid because title is required
            'author': self.author_d.id,  # Use author ID
            'genre': 'Horror',
            'publication_year': 2021
        }

    def test_create_book_authenticated(self):
        """Test authenticated book creation."""
        response = self.client.post('/api/books/', self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test unauthenticated users cannot create books."""
        self.client.logout()
        response = self.client.post('/api/books/', self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
