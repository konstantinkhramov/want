from django.urls import reverse
from rest_framework import test
from rest_framework import status


# Create your tests here.
from .models import Author


class AuthorTest(test.APITestCase):

    def setUp(self) -> None:
        self.author = Author(name='NameFirstTest', last_name='LastNameFirstTest')
        self.author.save()

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

    def test_get_author(self):
        response = self.client.get(reverse('author', args=(self.author.id,)))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_author(self):
        data = {
            'name': 'ChangeName',
            'last_name': self.author.last_name
        }
        response = self.client.put(reverse('author', args=(self.author.id,)), data=data)

        author = Author.objects.get(id=self.author.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(author.name, data['name'])

    def test_delete_author(self):

        response = self.client.delete(reverse('author', args=(self.author.id,)))

        author_list = list(Author.objects.all())

        self.assertEqual(author_list, [])
