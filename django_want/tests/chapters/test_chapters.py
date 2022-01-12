import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Books, Chapters
from books.serializers import ChapterSerializer
from users.models import User


class ChaptersTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username=f'user_test', password='123')
        self.user.refresh_from_db()
        self.client.force_authenticate(user=self.user, token=self.user.token)
        for i in range(1):
            Books.objects.create(book_caption=f'Book_{i}', user=self.user)

        self.book = Books.objects.first()

        chapter = Chapters.objects.create(book=self.book, caption='book parent',
                                          description='parent test1')
        chapter_child_1 = Chapters.objects.create(parent=chapter, caption='1 child', description='test1 child')
        chapter_child_2 = Chapters.objects.create(parent=chapter, caption='2 child', description='test1 child')
        chapter_child_3 = Chapters.objects.create(parent=chapter, caption='3 child', description='test1 child')
        chapter_child_empty = Chapters.objects.create(parent=chapter, caption='3 child', description='test1 child')

        chapter_child_1_child = Chapters.objects.create(parent=chapter_child_1, caption='child_1',
                                                        description='test child')
        chapter_child_2_child_1 = Chapters.objects.create(parent=chapter_child_2, caption='child_2_1',
                                                          description='test child')
        chapter_child_2_child_2 = Chapters.objects.create(parent=chapter_child_2, caption='child_2_2',
                                                          description='test child')
        chapter_child_3_child_1 = Chapters.objects.create(parent=chapter_child_3, caption='child_1',
                                                          description='test child')
        chapter_child_3_child_2 = Chapters.objects.create(parent=chapter_child_3, caption='child_2_1',
                                                          description='test child')
        chapter_child_3_child_3 = Chapters.objects.create(parent=chapter_child_3, caption='child_2_2',
                                                          description='test child')

        chapter.save()

        self.book.refresh_from_db()

    def test_get_chapter(self):
        chapter_id = self.book.chapters.first().id
        response = self.client.get(reverse('chapter', args=(chapter_id,)))
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['id'], chapter_id)

    def test_delete_chapters(self):
        chapters = self.book.chapters.all().prefetch_related('children')
        chapters_list = list(chapters)
        delete_chapter_id = chapters_list[0].children.first().id
        response = self.client.delete(reverse('chapter', args=(delete_chapter_id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        try:
            delete_chapter = Chapters.objects.get(pk=delete_chapter_id)
        except Chapters.DoesNotExist:
            delete_chapter = None

        self.assertEqual(None, delete_chapter)

    def test_update_chapters(self):
        chapter = Chapters.objects.get(pk=4)
        serializer = ChapterSerializer(chapter)
        data = serializer.data
        new_name = 'new name update'
        data['caption'] = new_name
        if data['book'] is None:
            data.pop('book')
        response = self.client.put(reverse('chapter', args=(chapter.id,)), data=data)
        chapter.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(chapter.caption, new_name)
