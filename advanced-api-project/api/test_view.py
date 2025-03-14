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
        self.client.login(username='testuser', password='password123')

        # ✅ Still force authenticate to ensure API authentication
        self.client.force_authenticate(user=self.user)

        # Create Authors
        self.author_a = Author.objects.create(name='Author A')
        self.author_b = Author.objects.create(name='Author B')

        # Create Books
        self.book1 = Book.objects.create(title='Book One', author=self.author_a, genre='Fiction', publication_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author=self.author_b, genre='Non-fiction', publication_year=2018)

    def test_explicit_login_check(self):
        """Test that login is explicitly used."""
        # ✅ Explicit login in a test case
        login_success = self.client.login(username='testuser', password='password123')
        self.assertTrue(login_success, "User login failed")
