from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Books, Chapters
from users.models import User


class BooksTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username=f'user_test', password='123')
        self.user.refresh_from_db()
        self.client.force_authenticate(user=self.user, token=self.user.token)
        for i in range(10):
            Books.objects.create(book_caption=f'Caption_{i}', user=self.user)

        self.book = Books.objects.first()

        chapter = Chapters.objects.create(book=self.book, caption='book parent',
                                          description='parent test1')
        chapter_child = Chapters.objects.create(parent=chapter, caption='one child', description='test1 child')

        chapter_child.save()

        self.book.refresh_from_db()

    def test_create_book(self):
        data = {'book_caption': 'Первая книга',
                'user': self.user.id,
                }
        response = self.client.post(reverse('books'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_not_permission(self):
        data = {'book_caption': 'Первая книга',
                'user': self.user.id,
                }
        self.client.logout()

        response = self.client.post(reverse('books'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('book', args=(self.book.id,)))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.patch(reverse('book', args=(self.book.id,)), data={'rating': 5})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(reverse('book', args=(self.book.id,)), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_books(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book(self):
        response = self.client.get(reverse('book', args=(self.book.id,)))
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['book_caption'], 'Caption_0')

    def test_patch_book(self):
        # Метод path позволяет обновить одно поле объекта
        response = self.client.patch(reverse('book', args=(self.book.id,)), data={'rating': 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book.refresh_from_db()

        self.assertEqual(self.book.rating, 5)

    def test_put_book(self):
        data = {
            'book_caption': 'Caption_new',
            'user': self.user.id,
            'rating': 1

        }
        response = self.client.put(reverse('book', args=(self.book.id,)), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book.refresh_from_db()

        self.assertEqual(self.book.book_caption, data['book_caption'])
        self.assertEqual(self.book.rating, data['rating'])

    def test_delete_book(self):
        response = self.client.delete(reverse('book', args=(self.book.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        try:
            book = Books.objects.get(pk=1)
        except Books.DoesNotExist:
            book = None
        self.assertEqual(book, None)

    def test_get_chapters(self):
        response = self.client.get(reverse('chapters', args=(self.book.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
