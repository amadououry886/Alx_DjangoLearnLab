from .models import Author, Book, Library, Librarian

#This query all the books for a specific author
Books = Book.objects.filter(author=author_name)

books = Library.objects.filter(name=Library_name)

librarian = Library.objects.get(name=Library_name)
