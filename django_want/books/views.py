from django.db.models import Max
from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Author, Books, Chapters, Parts

# Create your views here.
from .serializers import BooksSerializer, BookSerializerFull, ChapterSerializer, PartsSerializer


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


class BookViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Books.objects.all()
    serializer_class = BookSerializerFull

    @action(detail=True, methods=['get', 'post'])
    def chapters(self, request, pk=None, *args, **kwargs):
        if request.method == 'GET':
            if chapter_id := kwargs.get('chapter_id'):
                queryset = Chapters.objects.get(pk=chapter_id)
                serializer = ChapterSerializer(queryset,
                                               context={'request': request},
                                               many=False
                                               )
            else:
                queryset = Chapters.objects.filter(book_id=pk).all()
                serializer = ChapterSerializer(queryset,
                                               context={'request': request},
                                               many=True
                                               )
            return Response(serializer.data)
        if request.method == 'POST':
            data = request.data
            book = Books.objects.get(pk=pk)
            max_order_id = Chapters.objects \
                .filter(book_id=pk,
                        part_id__book_id=None) \
                .aggregate(max_order_id=Max('order_id')) \
                .get('max_order_id', 0)
            chapter = Chapters(caption=data.get('caption'),
                               description=data.get('description'),
                               order_id=data.get('order_id', max_order_id))
            book.chapters_set.add(chapter, bulk=False)

            return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get', 'post'])
    def parts(self, request, pk=None, *args, **kwargs):
        if request.method == 'GET':
            if parts_id := kwargs.get('parts_id'):
                queryset = Parts.objects.get(pk=parts_id)
                serializer = PartsSerializer(queryset,
                                             context={'request': request},
                                             many=False
                                             )
            else:
                queryset = Parts.objects.filter(book_id=pk).all()
                serializer = PartsSerializer(queryset,
                                             context={'request': request},
                                             many=True
                                             )
            return Response(serializer.data)
        if request.method == 'POST':
            data = request.data
            book = Books.objects.get(pk=pk)
            max_order_id = Parts.objects \
                .filter(book_id=pk) \
                .aggregate(max_order_id=Max('order_id')) \
                .get('max_order_id', 0)
            part = Parts(caption=data.get('caption'),
                         order_id=data.get('order_id', max_order_id))
            book.parts_set.add(part, bulk=False)

            return Response(status=status.HTTP_201_CREATED)
