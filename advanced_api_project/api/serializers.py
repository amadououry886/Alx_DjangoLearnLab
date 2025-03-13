from .models import Book, Author
from rest_framework import serializers
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        Model = Book
        fields = '__All__'

     
    def validate_publication_year(self, value):

        current_year = datetime.now().year
        if value > current_year: # The publication year should not be in the future
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value 


class AuthorSerializers(serializers.ModelSerializer):

    Books = BookSerializer(many=True, read_only=True)

    class Meta:

        fields = ['name', 'Books']