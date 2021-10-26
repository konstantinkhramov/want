from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate
from users.models import User


class BooksTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username=f'user_test', password='123')
        self.client.force_authenticate(user=self.user, token=self.user.token)

    def test_create_book(self):
        data = {'book_caption': 'Первая книга',
                'user_id': self.user.id,
                }
        response = self.client.post(reverse('books'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
