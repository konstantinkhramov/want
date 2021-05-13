from django.urls import reverse
from rest_framework import test
from rest_framework import status


# Create your tests here.

class AuthorTest(test.APITestCase):

    def test_create_author(self):
        data = {
            'name': 'AuthorName',
            'last_name': 'AuthorLastName'
        }

        response = self.client.post(reverse('authors'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        print(self.test_create_author.__name__, f'\n response:{response.json()}')

    def test_get_list_authors(self):
        self.test_create_author()

        response = self.client.get(reverse('authors'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        print(self.test_get_list_authors.__name__,  f'\n response:{response.json()}')
