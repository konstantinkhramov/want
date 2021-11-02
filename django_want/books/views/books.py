from django.db.models import Max
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from ..models import Books, Chapters

# Create your views here.
from ..serializers import BooksSerializer, BookSerializerFull, ChapterSerializer


class BookList(ListCreateAPIView):
    """
        Представление получения списка всех книг.
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookView(RetrieveUpdateDestroyAPIView):
    """
        Представление получение, обновления, и удаления книги произведения.
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Books.objects.all()
    serializer_class = BookSerializerFull


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Books.objects.all()
    serializer_class = BookSerializerFull

    @action(detail=True, methods=['get', 'post'])
    def chapters(self, request, pk=None, *args, **kwargs):
        if request.method == 'GET':
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
                .filter(book_id=pk) \
                .aggregate(max_order_id=Max('order_id')) \
                .get('max_order_id', 0)
            chapter = Chapters(caption=data.get('caption'),
                               description=data.get('description'),
                               order_id=data.get('order_id', max_order_id))
            book.chapters.add(chapter, bulk=False)

            return Response(status=status.HTTP_201_CREATED)
