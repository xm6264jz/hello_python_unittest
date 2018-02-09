from unittest import TestCase
from unittest.mock import patch

import movie
from movie import movie_rating, OMDB_Exception, omdb_call

class Test_OMDB_API(TestCase):

    def setUp(self):

        # TODO run the mock API server before running the tests.

        # For json-server
        # cd to the mock_omdb_api_json_server directory and run
        # json-server --watch movies.json --middlewares omdb.js --routes routes.json

        # For the mock python HTTP server, cd to mock_ombd_api_python_server
        # python mock_omdb.py

        # Control+C to stop either server.

        # replace the movie API with the mock api URL. If you use a different port, then modify this URL.
        movie.movie_base_url = 'http://127.0.0.1:3000/movies'


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
