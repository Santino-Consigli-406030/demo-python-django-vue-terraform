from sqlite3 import Date
from ..models import Book

def get_all_books():
    books = Book.objects.all().values('id', 'title', 'author', 'published_date')
    return list(books)

def create_book(data):
    validate_data(data)
    book = Book.objects.create(
        title = data.get('title'),
        author = data.get('author'),
        published_date = data.get('published_date')
    )
    return book

def validate_data(data):
    book = Book.objects.filter(title=data.get('title'))
    if book.exists():
        raise Exception('Book already exists')
    if data.get('title') == '':
        raise Exception('Title is required')
    if data.get('author') == '':
        raise Exception('Author is required')
    if data.get('published_date') == '':
        raise Exception('Published date is required')
    if not isinstance(data.get('published_date'), str):
        raise Exception('Published date must be a string')
    if data.get('published_date') > Date.today():
        raise Exception('Published date must be in the past')