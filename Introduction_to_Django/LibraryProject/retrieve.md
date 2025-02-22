# Command: Retrieve and display all attributes of the book you just created.

books = Book.objects.get(publication_year=1949)
for book in books:
    print(f"{book.title} written by {book.author} in {book.publication_year}")

# output: 1984 written by George Orwell in 1949
