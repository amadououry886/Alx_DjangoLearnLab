from django.db import models

# Create your models here.

class Author(models.Model):
    """
    The Author model represents a book author.

    Fields:
    - name: A string field storing the author's name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model represents a book written by an author.

    Fields:
    - title: A string field storing the book's title.
    - publication_year: An integer field storing the book's publication year.
    - author: A ForeignKey linking to the Author model, establishing a one-to-many relationship.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100, default="Unknown")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
