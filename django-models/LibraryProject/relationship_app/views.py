from django.shortcuts import render
from .models import Book  # Import the Book model
from django.views.generic.detail import DetailView
from .models import Library  # Import the Library model
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import render

def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template to render
    context_object_name = 'library'  # The name to use in the template

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in
            return redirect('list_books')  # Redirect to books page
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html', {"message": "Welcome, Librarian!"})

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html', {"message": "Welcome, Member!"})

