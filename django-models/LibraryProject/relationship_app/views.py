from django.shortcuts import render
from .models import Book  # Import the Book model
from django.views.generic.detail import DetailView
from .models import Library  # Import the Library model

def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template to render
    context_object_name = 'library'  # The name to use in the template
