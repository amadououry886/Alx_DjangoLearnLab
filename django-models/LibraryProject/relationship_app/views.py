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

# Helper function to check if user is an Admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    def admin_view(request):
    if not is_admin(request.user):
        return HttpResponseForbidden("You do not have permission to access this page.")
    return render(request, 'admin_dashboard.html')

