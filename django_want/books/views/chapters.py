from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from books.models import Chapters
from books.serializers import ChapterSerializer


class ViewChapters(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Chapters.objects.all()
    serializer_class = ChapterSerializer
