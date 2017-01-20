import unittest
from unittest.mock import Mock, patch
import guest_list
import builtins


class TestGuestListUI(unittest.TestCase):

    ''' Test the user interface of the program. Includes various ways of patching the
    guest_list.display_menu function'''

    # Use @patch decorators to patch the entire run of this test function.
    # These will create a Mock object, and replace the named function with the Mock.
    # Actually a MagicMock, which is a Mock with most of the configuration done for you.
    # It will automatically unpatch when function is done.

    # Mock display_menu to return user's choices. Provide side_effect values - the value
    # returned by the function every time it's called. This will simulate
    # user selecting 2, then 1, then q

    # Patch input. Every time input is called, it returns 'bob'.
    # The regular display_menu method calls input, but since that's been replaced
    # with a Mock that doesn't do anything except return the provided values,
    # don't need to worry about providing return vals for that.

    # And then patch the print function. Don't need to control the arguments,
    # but do care what it's called with.

    # Notice you need to provide each mock as an argument to the test.
    # Provide the mocks in reverse order to the order of the decorators.
    # And you'll need the mocks if you want to find out how the mock was used,
    # e.g. query the call_args for any of them.
    @patch('guest_list.display_menu', side_effect=['2', '1', 'q'])
    @patch('builtins.input', return_value='bob')
    @patch('builtins.print')
    def test_user_enters_new_guest(self, mock_print, mock_input, mock_menu):

        # User sees menu
        guest_list.guests = []

        # Call main function to start program.
        guest_list.main()

        # assert user was asked for guest's name - that input was called with this string
        mock_input.assert_called_with('Enter new guest name: ')

        # Assert new guest name is in list
        self.assertTrue('bob' in guest_list.guests)

        # Assert new guest's name was displayed
        mock_print.assert_any_call('bob')

        # Assert total number of guest names displayed is correct
        mock_print.assert_any_call('Total 1 guest(s)')

        # Assert that program printed the quit message .
        mock_print.assert_called_with('Bye!')



    # This function uses context managers to patch input, guest_list.display_menu, and print.

    def test_user_adds_and_then_deletes_guests(self):

        guest_list.guests = []

        # Patching with a context manager. With this approach, can control the scope of the patch.
        # Although can have a lot of nested calls if several patches are applied

        # Side effects: Add bob and alice. Delete bob. Delete eve (who isn't in the list). Display whole list. quit.
        with patch('guest_list.display_menu', side_effect=['2', '2', '3', '3', '1', 'q']):

            # Patch input. Configure side effects to set up return values from mock_input.
            # Add bob, add alice, delete bob, delete eve
            with patch('builtins.input', side_effect=['bob', 'alice', 'bob', 'eve']) as mock_input:

                #And patch print.
                with patch('builtins.print') as mock_print:

                    guest_list.main()

                    # Verify contents of guest list
                    self.assertFalse('eve' in guest_list.guests)  # Eve should NOT be in the list
                    self.assertFalse('bob' in guest_list.guests)  # Bob should NOT be in the list
                    self.assertTrue('alice' in guest_list.guests) # Alice should be in the list

                    # Assert total number of guests displayed is 1
                    mock_print.assert_any_call('Total 1 guest(s)')
                    # Assert message about removing bob
                    mock_print.assert_any_call('bob removed')
                    # Assert message that eve was not found
                    mock_print.assert_any_call('eve was not found in the guest list')

                    mock_print.assert_called_with('Bye!')

                    print('you won\'t see this') # Because we've replaced the built in print function with our mock

        # Once the context manager ends, the patch is automatically unpatched, and the original function will be restored.
        print('but you will see this')  # So you'll see this printed to the terminal.



    # Can create Mock objects manually; and patch manually. Need to remember to unpatch!

    # Patch with a mock input to provide some input values
    # And a mock print function, to check what was printed

    @patch('builtins.input', side_effect=['alice', 'zed'])
    @patch('builtins.print')
    def test_search_for_a_guest(self, mock_print, mock_input):

        # Example guest list
        guest_list.guests = ['bob', 'alice']
        # assert searching displays found message for alice, but not for zed.

        # Save a reference to the function that is about to be patched
        menu_function = guest_list.display_menu

        # replace display_menu with a mock function, with side effect to return search, search, quit.
        guest_list.display_menu = Mock(side_effect=['4', '4', 'q'])

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

        # Restore display_menu
        guest_list.display_menu = menu_function


if __name__ == '__main__':
    unittest.main()
