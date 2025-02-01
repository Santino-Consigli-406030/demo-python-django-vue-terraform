from django.urls import path
from .views import viewsBook as views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/data/', views.get_data, name='get_data'),
    path('api/books/', views.get_all_books, name='get_all_books'),
    path('api/books/create',views.create_book, name='create_book'),
]