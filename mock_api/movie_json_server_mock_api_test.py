from unittest import TestCase
from unittest.mock import patch, Mock

import movie
from movie import movie_rating, OMDB_Exception, omdb_call

class Test_OMDB_API(TestCase):

    def setUp(self):
        # replace the movie API with json-server api
        movie.base_url = 'http://127.0.0.1:3000/movies'

    def test_get_movie_rating(self):
        response = movie_rating('Frozen')
        self.assertEqual('7.5/10', response)


    def test_get_movie_rating_not_found(self):
        with self.assertRaises(OMDB_Exception) as ex_context:
            movie.movie_rating('Nope')
        self.assertEqual("Movie not found!", str(ex_context.exception))


    # Was exception thrown if OMBD key not present?
    def test_get_movie_no_API_key(self):
        with patch.dict('os.environ', {'OMDB_KEY': ''}):
            with self.assertRaises(movie.OMDB_Exception) as ex_context:
                response = movie_rating('Frozen')  # Real movie
                print(response)
            self.assertEqual('No API key provided.', str(ex_context.exception))
