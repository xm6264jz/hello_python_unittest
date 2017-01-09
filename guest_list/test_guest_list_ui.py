import unittest
from unittest.mock import Mock
import guest_list


class TestGuestListUI(unittest.TestCase):

    def test_user_enters_new_guest(self):

        # User sees menu
        guest_list.guests = []

        # Mock display_menu to return user's choices
        # User will select 2, then 1, then q
        guest_list.display_menu = Mock(side_effect=['2', '1', 'q'])

        mock_input = Mock(return_value='bob')
        guest_list.input = mock_input

        mock_print = Mock()
        guest_list.print = mock_print

        guest_list.main()

        # assert user was asked for guest's name - that input was called with
        mock_input.assert_called_with('Enter new guest name: ')

        # Assert new guest name is in list
        self.assertTrue('bob' in guest_list.guests)

        # Assert new guest's name was displayed
        mock_print.assert_any_call('bob')

        # Assert total number of guest names displayed is correct
        mock_print.assert_any_call('Total 1 guest(s)')

        mock_print.assert_called_with('Bye!')


    def test_user_adds_and_then_deletes_guests(self):

        guest_list.guests = []

        # Add bob and alice. Delete bob. Delete eve (who isn't in the list). Display whole list. quit.
        guest_list.display_menu = Mock(side_effect=['2', '2', '3', '3', '1', 'q'])

        # Add bob, add alice, delete bob, delete eve
        mock_input = Mock(side_effect=['bob', 'alice', 'bob', 'eve'])
        guest_list.input = mock_input

        mock_print = Mock()
        guest_list.print = mock_print

        guest_list.main()

        # Verify contents of guest list
        self.assertFalse('eve' in guest_list.guests)
        self.assertFalse('bob' in guest_list.guests)
        self.assertTrue('alice' in guest_list.guests)

        # Assert total number of guests displayed is 1
        mock_print.assert_any_call('Total 1 guest(s)')
        # Assert message about removing bob
        mock_print.assert_any_call('bob removed')
        # Assert message that eve was not found
        mock_print.assert_any_call('eve was not found in the guest list')

        mock_print.assert_called_with('Bye!')


    def test_search_for_a_guest(self):

        # Example guest list
        guest_list.guests = ['bob', 'alice']

        # assert searching displays found message for alice, but not for zed.
        guest_list.display_menu = Mock(side_effect=['4', '4', 'q'])

        # A mock input to provide some input values
        mock_input = Mock(side_effect=['alice', 'zed'])
        guest_list.input = mock_input

        # And a mock print function, to check what was printed
        mock_print = Mock()
        guest_list.print = mock_print

        #Run the program
        guest_list.main()

        # What was printed? Get a list of things print (mock_print) was called with
        printcalls = mock_print.call_args_list   # A list of tuples: the arguments used each time the function is called

        # Assert message about alice found
        self.assertEqual(printcalls[0], ('alice is in your list', ))

        # Followed by message that zed not found
        self.assertEqual(printcalls[1], ('zed is not in your list', ))





if __name__ == '__main__':
    unittest.main()
