
from rest_framework import generics, status, permissions, filters as drf_filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework as filters

# ListView: Retrieve all books (Read-Only)
class BookListView(generics.ListAPIView):
    """
    API endpoint that allows users to retrieve a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]  # Fixed this line
    # Step 1: Filtering by specific fields (change fields according to your model)
    filterset_fields = ['genre', 'publication_year', 'author']

    # Step 2: Searching by title and author
    search_fields = ['title', 'author__name']

    # Step 3: Ordering by fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

# DetailView: Retrieve a single book by ID (Read-Only)
class BookDetailView(generics.RetrieveAPIView):
    """
    API endpoint that retrieves details of a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView: Add a new book (Requires Authentication)
class BookCreateView(generics.CreateAPIView):
    """
    API endpoint for authenticated users to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Custom method to handle book creation, ensuring proper validation.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# UpdateView: Modify an existing book (Requires Authentication)
class BookUpdateView(generics.UpdateAPIView):
    """
    API endpoint for authenticated users to update book details.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# DeleteView: Remove a book (Requires Authentication)
class BookDeleteView(generics.DestroyAPIView):
    """
    API endpoint for authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
