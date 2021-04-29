import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class AuthenticationTests(APITestCase):
    def setUp(self) -> None:
        self.list_user = [User.objects.create_user(username=f'user_{x}', password='123') for x in range(10)]

    def test_create_user(self):
        data = {
            'username': 'kostya',
            'password': '123',
        }
        response = self.client.post(reverse('user_register'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_users(self):
        self.test_create_user()
        user = User.objects.get(username='kostya')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user.token)
        response = self.client.get(reverse('users'))
        json_object = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_user(self):
        self.test_create_user()
        data = {
            'username': 'kostya',
            'password': '123'
        }

        response = self.client.post(reverse('user_login'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)