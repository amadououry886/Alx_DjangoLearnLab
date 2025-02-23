from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Library, Author, Librian, Book
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.

def Book_views(request):

    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books}))


class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # This makes `library` available in the template



# Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('list_books')  # Redirect to book list or homepage
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

