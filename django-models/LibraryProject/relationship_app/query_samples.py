from .models import Author, Book, Library, Librarian

#This query all the books for a specific author
Books = Book.objects.filter(author="Machiavel")

books = Library.objects.filter(name="AIU_Library")

librarian = Library.objects.get(name="Nur_Sharrifah")
