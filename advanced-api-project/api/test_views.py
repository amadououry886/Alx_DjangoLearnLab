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

    def test_list_books(self):
        """Test retrieving the list of books."""
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_books_by_genre(self):
        """Test filtering books by genre."""
        response = self.client.get('/api/books/', {'genre': 'Fiction'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_search_books_by_title(self):
        """Test searching books by title."""
        response = self.client.get('/api/books/', {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_order_books_by_year(self):
        """Test ordering books by publication year."""
        response = self.client.get('/api/books/', {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book Two')  # Oldest first

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

    def test_update_book_authenticated(self):
        """Test updating a book by an authenticated user."""
        update_data = {
            'title': 'Updated Book',
            'author': self.author_a.id,  # Use author ID
            'genre': 'Fiction',
            'publication_year': 2020
        }
        response = self.client.put(f'/api/books/{self.book1.id}/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book_authenticated(self):
        """Test deleting a book by an authenticated user."""
        response = self.client.delete(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        """Test unauthenticated users cannot delete books."""
        self.client.logout()
        response = self.client.delete(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
