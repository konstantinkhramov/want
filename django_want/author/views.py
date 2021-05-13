from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Author
from .serializers import AuthorSerializer
# Create your views here.


class AuthorList(ListCreateAPIView):
    """
        Представление получения списка всех автаров и создания авторов.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
