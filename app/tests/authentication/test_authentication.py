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
        v = 1