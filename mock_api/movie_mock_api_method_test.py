from unittest import TestCase
from unittest.mock import patch, Mock

import movie
from movie import movie_rating, OMDB_Exception, omdb_call

class Test_OMDB_API(TestCase):


    # Patching with a decorator. Creates a mock for the designated function for the duration of this test, unpatches at the end
    # Note the second argument to the test function is required, makes the Mock object available to the test
    @patch('movie.omdb_call', return_value = {'Response': 'True', 'Ratings': [{'Value': '7.5/10', 'Source': 'Internet Movie Database'}]} )
    def test_get_movie_rating_patch(self, api_patch):
        response = movie_rating('Example Movie')
        self.assertEqual('7.5/10', response)


    # Same test, but uses a mock
    def test_get_movie_rating_mock(self):

        # Create a mock and replace movie.omdb_call with the Mock function
        mock_api = Mock(return_value = {'Response': 'True', 'Ratings': [{'Value': '7.5/10', 'Source': 'Internet Movie Database'}]} )
        movie.omdb_call = mock_api
        response = movie_rating('Example Movie')
        self.assertEqual('7.5/10', response)

        # If needed, can check how the mock was called. For example, was it called at all?
        mock_api.assert_called()   # New in python 3.6 so check version and upgrade if needed.
        # See documentation for checking for a certain number of calls, verifying mock was called with expected arguments.


    # Same test, but uses patch as a context manager
    def test_get_movie_rating_patch_decorator(self):
        with patch('movie.omdb_call', return_value = {'Response': 'True', 'Ratings': [{'Value': '7.5/10', 'Source': 'Internet Movie Database'}]} ) as mock_api:
            response = movie_rating('Example Movie')
            self.assertEqual('7.5/10', response)

        # At this point in time, the patch is no longer applied. Use this approach if you only need to patch for part of a test.


    # Some more tests - was exception thrown if request errors?
    # Raise general exception from omdb_call
    @patch('movie.omdb_call', side_effect=Exception)
    def test_get_movie_rating_error_connecting(self, api_patch):
        with self.assertRaises(movie.OMDB_Exception) as ex_context:
            response = movie_rating('Example Movie')
        self.assertEqual('Error connecting to OMDB', str(ex_context.exception))


    # Was exception thrown if response contains an error?
    @patch('movie.omdb_call', side_effect=[{'Response':'False', 'Error':'Something went wrong'}])
    def test_get_movie_rating_error_returned_in_response(self, api_patch):

        with self.assertRaises(movie.OMDB_Exception) as ex_context:
            response = movie_rating('Example Movie')

        self.assertEqual('Something went wrong', str(ex_context.exception))


    # Expect an exception thrown if json is not in expected format for Ratings
    @patch('movie.omdb_call', return_value = {'Ratings': '7.5'} )
    def test_get_movie_rating_ratings_incorrect_format(self, api_patch):
        with self.assertRaises(OMDB_Exception) as ex_context:
            movie.movie_rating('example')
        self.assertEqual("Error processing response from OMDB", str(ex_context.exception))


    # Expect an exception thrown if json is not in expected format for Ratings
    @patch('movie.omdb_call', return_value = {'Ratings': [] } )
    def test_get_movie_rating_no_ratings_returned(self, api_patch):
        with self.assertRaises(OMDB_Exception) as ex_context:
            movie.movie_rating('example')
        self.assertEqual("Error processing response from OMDB", str(ex_context.exception))


    # Expect an exception thrown if json is not in expected format for Ratings or response
    @patch('movie.omdb_call', return_value = {'Donut': 'Sprinkles'} )
    def test_get_movie_rating_no_response_or_rating(self, api_patch):
        with self.assertRaises(OMDB_Exception) as ex_context:
            movie.movie_rating('example')
        self.assertEqual("Error processing response from OMDB", str(ex_context.exception))
