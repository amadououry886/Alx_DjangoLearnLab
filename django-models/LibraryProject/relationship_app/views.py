from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Library, Author, Librian, Book


# Create your views here.

def Book_views(request):

    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books}))


class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # This makes `library` available in the template

