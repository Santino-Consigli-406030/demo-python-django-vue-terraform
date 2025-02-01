from ..models import Book

def get_all_books():
    books = Book.objects.all().values('id', 'title', 'author', 'published_date')
    return list(books)

def create_book(data):
    book = Book.objects.create(
        title = data.get('title'),
        author = data.get('author'),
        published_date = data.get('published_date')
    )
    return book