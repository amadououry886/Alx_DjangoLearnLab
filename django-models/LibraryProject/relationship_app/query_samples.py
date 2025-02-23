import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Retrieve all books by a specific author."""
    author = Author.objects.get(name=author_name).first()
    if author:
        books = Book.objects.filter(author=author)  # Corrected: using `author` object, not a string
        return [book.title for book in books]
    return []

def list_books_in_library(library_name):
    """List all books available in a specific library."""
    try:
        library = Library.objects.get(name=library_name)  # Corrected: Use `.get()`, since only one library should match
        return [book.title for book in library.books.all()]  # Corrected: `.all()` is necessary for ManyToMany relationships
    except Library.DoesNotExist:
        return []

def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian managing a specific library."""
    try:
        library = Library.objects.get(name=library_name)  # Corrected: `.get()`, assuming each library has one librarian
        return library.librarian.name  # Corrected: Access the `Librarian` via the reverse OneToOne relationship
    except Library.DoesNotExist:
        return "Library not found"
    except Librarian.DoesNotExist:
        return "No librarian assigned"

if __name__ == "__main__":
    print("Books by J.K. Rowling:", query_books_by_author("J.K. Rowling"))
    print("Books in Central Library:", list_books_in_library("Central Library"))
    print("Librarian of Central Library:", retrieve_librarian_for_library("Central Library"))

