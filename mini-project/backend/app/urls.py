from .views import viewsBook as views
from django.urls import path
from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(
    title="Snippets API",
    description="Test description",
    version="v1",
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/data/', views.get_data, name='get_data'),
    path('api/books/', views.get_books_view, name='get_all_books'),
    path('api/books/create', views.create_book_view, name='create_book'),
    path('schema/', schema_view, name='openapi-schema'),
    path('docs/', include_docs_urls(title='Snippets API')),
]