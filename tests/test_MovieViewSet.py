from django.test import TestCase, Client

from film.models import Movie, Actor
from datetime import date


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        self.actor = Actor.objects.create(name='Test actor', birthdate=date(2023,6,1) )
        self.movie = Movie.objects.create(
            name='Test Movie',
            imdb=3.5,
            genre='Horror',
            year=2015
        )
        self.client = Client()


    def test_return_all_movies(self):
        response = self.client.get('/movies/')
        data = response.data

        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEqual(data[0]['name'], 'Test Movie')

    def test_search_movie(self):
        response = self.client.get('/movies/?search=Test')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Test Movie')

    def test_ordering(self):
        response = self.client.get('/movies/?ordering=imdb')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['imdb'], 3.5)
        print(data)

