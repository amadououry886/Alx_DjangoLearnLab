from django.db import models

# Create your models here.

"""This is the Author class it gonna store the name """

class Author(models.Mode):

    name = models.CharField(max_length=20)

    def __str__(self):

        return self.name

"""This is the Book class it gonna store the title, book and the foreinKey of the the Author"""

class Book(models.Model):

    title = models.CharField(max_length=20)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):

        return self.title