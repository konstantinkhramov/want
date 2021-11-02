from rest_framework import serializers
from ..models import Chapters


class ChildChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapters
        fields = ['id', 'book', 'order', 'caption', 'description']


class ChapterSerializer(serializers.ModelSerializer):
    children = ChildChapterSerializer(required=False, many=True)

    class Meta:
        model = Chapters
        fields = ['id', 'book', 'children', 'order', 'caption', 'description']
