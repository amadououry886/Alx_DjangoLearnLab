# import Book
from bookshelf.models import Book

# Delete the book you created and confirm the deletion by trying to retrieve all books again.

book = Book.objects.get(publication_year=1949)
book.delete()

books = Book.objects.all()
for book in books:
    print(book)
