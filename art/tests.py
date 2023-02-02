from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Art


class ArtTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        tester = get_user_model().objects.create_user(
            username='tester', password='password'
        )
        tester.save()

        art_create = Art.objects.create(
            owner=tester,
            artist='Rene Magritte',
            artwork_name='This is Not a Pipe',
            description='Painting of a pipe.',
        )
        tester.save()

    def setUp(self):
        self.client.login(username='tester', password='password')

    def test_art_model(self):
        art = Art.objects.get(id=1)
        self.assertEqual(str(art.owner), 'tester')
        self.assertEqual(str(art.artist), 'Rene Magritte')
        self.assertEqual(str(art.description), 'Painting of a pipe.')
        self.assertEqual(str(art.artwork_name), 'This is Not a Pipe')

    def test_create_art(self):
        data = {'owner': 1, 'artist': 'Andy Warhol', 'artwork_name': 'Nine Jackies',
                'description': 'Silkscreen of Jackie Kennedy'}
        response = self.client.post(reverse('art_list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # test get of created artwork
        self.assertEqual(len(Art.objects.all()), 2)
        self.assertEqual(Art.objects.get(id=2).artwork_name, 'Nine Jackies')

    def test_update_thing(self):
        url = reverse("art_detail", args=(1,))
        data = {'owner': 1, 'artist': 'Rene Magritte', 'artwork_name': 'This is Not a Pipe',
                'description': 'Surrealist painting of a pipe.'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        art = Art.objects.get(id=1)
        self.assertEqual(art.description, data["description"])

    def test_delete_art(self):
        response = self.client.delete(reverse('art_detail', args=(1,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Art.objects.all()), 0)

    def test_authentication_required(self):
        self.client.logout()
        response = self.client.get(reverse('art_list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
