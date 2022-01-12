from django.urls import path, include

urlpatterns = [
    path('', include('books.urls.books')),
    path('', include('books.urls.chapters'))
]
