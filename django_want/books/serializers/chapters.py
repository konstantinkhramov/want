from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from ..models import Chapters


class ChildChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapters
        fields = ['id', 'book', 'order', 'caption', 'description']


# Еще один способ рекурсивной сериализации через стороннюю библиотеку
# class ChapterSerializer(serializers.ModelSerializer):
#     children = serializers.ListSerializer(read_only=True, child=RecursiveField())
#
#     class Meta:
#         model = Chapters
#         fields = ['id', 'book', 'children', 'order', 'caption', 'description']


class ChapterSerializer(serializers.ModelSerializer):
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())

    class Meta:
        model = Chapters
        fields = ['id', 'book', 'children', 'order', 'caption', 'description']

        def get_related_field(self, model_field):
            # Рекурсивная сериализация Django Native
            # Handles initializing the `subcategories` field
            return ChapterSerializer()
