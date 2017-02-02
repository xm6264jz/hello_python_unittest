import unittest
from unittest.mock import patch
import dice

class TestDice(unittest.TestCase):

    @patch('dice.roll', return_value=4)
    def test_play_user_wins(self, mock_roll):
        self.assertFalse(dice.play())

    @patch('dice.roll', return_value=6)
    def test_play_user_wins(self, mock_roll):
        self.assertTrue(dice.play())

    @patch('dice.roll', return_value=6)
    @patch('builtins.print')
    def test_main_user_wins(self, mock_print, mock_roll):

        dice.main()
        # assert print called with 'you win!'
        mock_print.assert_any_call('you win!')

    @patch('random.randint', return_value=4)
    def test_roll(self, mock_random):
        self.assertTrue(4, dice.roll())
