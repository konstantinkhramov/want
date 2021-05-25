from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Author, Books

# Create your views here.
from .serializers import BooksSerializer, BookSerializerFull


class BookList(ListCreateAPIView):
    """
        Представление получения списка всех книг.
    """

    # permission_classes = [permissions.IsAuthenticated]
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookView(RetrieveUpdateDestroyAPIView):
    """
        Представление получение, обновления, и удаления книги произведения.
    """

    # permission_classes = [permissions.IsAuthenticated]
    queryset = Books.objects.all()
    serializer_class = BookSerializerFull
