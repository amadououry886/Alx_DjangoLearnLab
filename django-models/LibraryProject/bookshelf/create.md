# Command: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

# import book table
from bookshelf.models import Book

# Create with an object
book = Book.objects.create(
    title = '1984',
    author = 'George Orwell',
    publication_year = '1949'
)
