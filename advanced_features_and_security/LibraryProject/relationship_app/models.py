from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomerUserManager

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='image_folder', blank=True, null=True)
    objects = CustomerUserManager()

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_add_book", "can_add_book"),
            ("can_change_book", "can_edit_book"),
            ("can_delete_book", "can_delete_book"),
        ]

    def __str__(self):
        return self.title

#User class
class UserProfile(models.Model):
    # Choices
    ROLES = (
            ('Admin', 'Admin'),
            ('Librarian', 'Librarian'),
            ('Member', 'Member'),
            )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES, default='Member')


# Create your models here.
class Author(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
