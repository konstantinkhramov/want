from rest_framework import serializers
from author.serializers import AuthorSerializer
from .chapters import ChapterSerializer
from ..models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class BookSerializerFull(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    chapters = ChapterSerializer(required=False, many=True)

    class Meta:
        model = Books
        fields = ['author', 'book_caption', 'chapters', 'rating', 'create_date', 'description']
