import unittest
import guest_list

class TestGuestList(unittest.TestCase):

    def test_add_a_guest(self):
        example_guests = ['alice', 'zack']
        guest_list.guests = example_guests
        guest_list.add_guest('bob')
        expected_guest_list = ['alice', 'bob', 'zack']

        self.assertEqual(guest_list.guests, expected_guest_list)


    def test_delete_a_guest(self):
        example_guests = ['alice', 'bob', 'zack']
        guest_list.guests = example_guests
        guest_list.remove_guest('bob')
        expected_guest_list = ['alice', 'zack']

        self.assertEqual(guest_list.guests, expected_guest_list)


    def test_guest_is_in_list(self):

        example_guests = ['alice', 'zack']
        guest_list.guests = example_guests

        self.assertTrue(guest_list.guest_in_list('alice'))
        self.assertFalse(guest_list.guest_in_list('bob'))


if __name__ == '__main__':
    unittest.main()
