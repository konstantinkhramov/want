from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Author
from .serializers import AuthorSerializer


# Create your views here.


class AuthorList(ListCreateAPIView):
    """
        Представление получения списка всех автаров и создания авторов.
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorView(RetrieveUpdateDestroyAPIView):
    """
        Представление получение, обновления, и удаления автора произведения.
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
