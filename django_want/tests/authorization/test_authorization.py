from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationTests(APITestCase):

    def test_create_account(self):
        """
            Ensure we can create a new account object.
        """
        url = reverse('register')
        data = {"username": "kostya",
                "password": "12345678qwerty"}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_token(self):
        """"
            Тест получения токена существующего пользователя
        """

        url = reverse('token')
        data = {"username": "kostya",
                "password": "12345678qwerty"}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh_token(self):
        """"
            Тест обновления токена
        """

        url = reverse('token')
        data = {"username": "kostya",
                "password": "12345678qwerty"}
        response = self.client.post(url, data, format='json')

        url = reverse('refresh_token')
        data = {'refresh_token': response.data['refresh_token']}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_revoke_token(self):
        """"
            Тестирование овтязки токена
        """

        url_token = reverse('token')
        data_token = {"username": "kostya",
                      "password": "12345678qwerty"}

        response = self.client.post(url_token, data_token, format='json')

        url_revoke = reverse('revoke_token')
        data_revoke = {
            'token': response.data['access_token']
        }

        response = self.client.post(url_revoke, data_revoke, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)