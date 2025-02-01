import json
from django.http import HttpResponse, JsonResponse
from ..services.bookService import *

def index(request):
    return HttpResponse("Welcome to the Bookstore!")

def get_data(request):
    data = {
        "message": "Hello, World!"
    }
    return JsonResponse(data)

def get_all_books(request):
    books = get_all_books_service()
    return JsonResponse(books, safe=False)

@csrf_exempt
def create_book(request):
    if request.method == 'POST':
            data = json.loads(request.body)
            title = data.get('title')
            author = data.get('author')
            published_date = data.get('published_date')
            bookSave = create_book(data)
            
            