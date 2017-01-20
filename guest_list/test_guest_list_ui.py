import unittest
from unittest.mock import Mock, patch
import guest_list
import builtins


class TestGuestListUI(unittest.TestCase):

    def test_user_enters_new_guest(self):

        # User sees menu
        guest_list.guests = []

        # Mock display_menu to return user's choices
        # User will select 2, then 1, then q
        guest_list.display_menu = Mock(side_effect=['2', '1', 'q'])

        # Patch input. Every time input is called, it returns 'bob'.
        # The regular display_menu method calls input, but since that's been replaced
        # with a Mock that doesn't do anything except return the provided values,
        # don't need to worry about providing return vals for that.
        with patch('builtins.input') as mock_input:

            mock_input.return_value='bob'

            with patch('builtins.print') as mock_print:

                # Call main function to start program.
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

        # Patch input.
        with patch('builtins.input') as mock_input:

            with patch('builtins.print') as mock_print:

                # Add bob and alice. Delete bob. Delete eve (who isn't in the list). Display whole list. quit.
                guest_list.display_menu = Mock(side_effect=['2', '2', '3', '3', '1', 'q'])

                # Set up return values from mock_input.
                # Add bob, add alice, delete bob, delete eve
                mock_input.side_effect = ['bob', 'alice', 'bob', 'eve']

                guest_list.main()

                # Verify contents of guest list
                self.assertFalse('eve' in guest_list.guests)  # Eve should NOT be in the list
                self.assertFalse('bDob' in guest_list.guests)  # Bob should NOT be in the list
                self.assertTrue('alice' in guest_list.guests) # Alice should be in the list

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
        # replace display_menu with a mock function to return search, search, quit.
        guest_list.display_menu = Mock(side_effect=['4', '4', 'q'])

        # A mock input to provide some input values
        with patch('builtins.input') as mock_input:
            # And a mock print function, to check what was printed
            with patch('builtins.print') as mock_print:

                # Configure return values from mock_input
                mock_input.side_effect = ['alice', 'zed']

                #Run the program
                guest_list.main()

                # What was printed? Get a list of things print (mock_print) was called with
                printcalls = mock_print.call_args_list   # A list of calls.  A call is a tuple of (arguments, kwordargs) used each time the function is called
                                                                # arguments is a tuple, kwordargs is a dictionary.
                call_alice = ( 'alice is in your list' , )
                # Assert message about alice found in the call_args_list
                self.assertEqual(printcalls[0][0], call_alice )

                # Followed by message that zed not found
                call_zed = ( 'zed is not in your list' , )
                self.assertEqual(printcalls[1][0], call_zed )



if __name__ == '__main__':
    unittest.main()
