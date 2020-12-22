import json

from django.contrib.auth.models import User
from django.urls import reverse
from oauth2_provider.models import Application
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationTests(APITestCase):

    @staticmethod
    def create_admin():
        """
            create super user admin 
                username='admin', password='123'
            return:
                User<admin>
            
        """
        admin = User.objects.create_superuser(username='admin', password='123')
        admin.save()

        return admin

    @staticmethod
    def create_app():
        """
            create app for oauth2

            return:
                Application<django_want>
        """
        admin = AuthenticationTests.create_admin()
        application = Application(user=admin,
                                  client_type=Application.CLIENT_CONFIDENTIAL,
                                  authorization_grant_type=Application.GRANT_PASSWORD,
                                  name='django_want'
                                  )
        application.save()

        return application

    def get_token(self):
        application = AuthenticationTests.create_app()

        CLIENT_ID = application.client_id
        CLIENT_SECRET = application.client_secret

        url = reverse('oauth2_provider:token')
        data = {'grant_type': Application.GRANT_PASSWORD,
                'username': 'admin',
                'password': '123',
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET
                }

        response = self.client.post(url, data)

        access_token = response.json()['access_token']

        return access_token

    def test_get_token_acces(self):
        """
            Ensure we can create a new account object.
        """

        application = AuthenticationTests.create_app()

        CLIENT_ID = application.client_id
        CLIENT_SECRET = application.client_secret

        url = reverse('oauth2_provider:token')
        data = {'grant_type': Application.GRANT_PASSWORD,
                'username': 'admin',
                'password': '123',
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET
                }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_token_password_error(self):
        application = AuthenticationTests.create_app()

        CLIENT_ID = application.client_id
        CLIENT_SECRET = application.client_secret

        url = reverse('oauth2_provider:token')
        data = {'grant_type': Application.GRANT_PASSWORD,
                'username': 'admin',
                'password': '123',
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET
                }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_list_users(self):
        token = self.get_token()
        self.client.credentials(Authorization=f' Bearer {token}')
        response = self.client.get(reverse('users'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
