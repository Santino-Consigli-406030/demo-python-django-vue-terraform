from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..services.bookService import get_all_books, create_book

@api_view(['GET'])
def index(request):
    return Response({"message": "Welcome to the Bookstore!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_data(request):
    data = {
        "message": "Hello, World!"
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_books_view(request):
    books = get_all_books()
    return Response(books, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_book_view(request):
    data = request.data
    bookSave = create_book(data)
    return Response(bookSave, status=status.HTTP_201_CREATED)