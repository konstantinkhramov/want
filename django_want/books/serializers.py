from rest_framework import serializers

from author.serializers import AuthorSerializer
from .models import Books, Chapters, Parts


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapters
        fields = ['id', 'part_id', 'order_id', 'caption', 'description']


class PartsSerializer(serializers.ModelSerializer):
    chapters_set = ChapterSerializer(many=True)

    class Meta:
        model = Parts
        fields = ['id', 'caption', 'order_id', 'chapters_set']


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class BookSerializerFull(serializers.ModelSerializer):
    author_id = AuthorSerializer()
    parts_set = PartsSerializer(many=True)
    chapters_set = ChapterSerializer(many=True)

    class Meta:
        model = Books
        fields = ['author_id', 'parts_set', 'chapters_set', 'book_caption', 'rating', 'create_date', 'description']
