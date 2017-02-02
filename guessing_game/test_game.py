import unittest
from unittest.mock import patch, call
import game


class TestGame(unittest.TestCase):


    @patch('game.get_secret_number', return_value=4)
    @patch('game.get_guess', side_effect=[3, 10, 4])
    @patch('builtins.print')
    def test_play_game(self, mock_print, mock_guesses, mock_secret):

        game.main()

        # Create a list of expected call objects. These will be compared to the actual calls made
        # to the mock_print method. 
        expected_calls = [ call('too low!') , call('too high!') , call('Correct!') ]
        self.assertEqual(expected_calls, mock_print.call_args_list)


if __name__ == '__main__':
    unittest.main()


