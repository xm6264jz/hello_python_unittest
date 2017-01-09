import unittest
from unittest.mock import Mock

import recycling

class TestRecycling(unittest.TestCase):

    def test_int_input(self):
        pass


    def test_max_values(self):

        # More than one house with the same max value
        example_data = [1, 3, 5, 0, 2, 6, 3, 6]
        max_data = recycling.max_recycling(example_data)
        self.assertEqual(max_data.crates, 6)
        self.assertEqual(max_data.houses, [5, 7])

        # Single max value
        example_data = [1, 3, 9, 0, 2, 3, 3, 6]
        max_data = recycling.max_recycling(example_data)
        self.assertEqual(max_data.crates, 9)
        self.assertEqual(max_data.houses, [2])


    def test_min_values(self):

        # More than one joint min value
        example_data = [1, 0, 3, 5, 0, 2, 6]
        min_data = recycling.min_recycling(example_data)
        self.assertEqual(min_data.crates, 0)
        self.assertEqual(min_data.houses, [1, 4])

        # Single min value
        example_data = [1, 3, 5, 0, 2, 6]
        min_data = recycling.min_recycling(example_data)
        self.assertEqual(min_data.crates, 0)
        self.assertEqual(min_data.houses, [3])


    def test_total(self):
        example_data = [1, 3, 5, 0, 2, 6]
        self.assertEqual(recycling.total_crates(example_data), 17)


    def test_get_crate_quantities(self):
        example_data = [1, 3, 5, 0, 2, 6]
        mock_input = Mock(side_effect=example_data)
        recycling.input = mock_input
        self.assertEqual(recycling.get_crate_quantities(6), example_data)

        recycling.input = __builtins__.input  # Replace original input


    def test_int_input(self):

        example_invalid_inputs = ['-2', '-1000', 'abc', '123abc', '3']  # Put a valid input at the end or the function will never return
        recycling.input = Mock(side_effect=example_invalid_inputs)
        self.assertEqual(recycling.positive_int_input('example question'), 3)

        example_valid_inputs = [ '0', '13', '1', '100000000']
        recycling.input = Mock(side_effect=example_valid_inputs)
        self.assertEqual(recycling.positive_int_input('example question'), 0)
        self.assertEqual(recycling.positive_int_input('example question'), 13)
        self.assertEqual(recycling.positive_int_input('example question'), 1)
        self.assertEqual(recycling.positive_int_input('example question'), 100000000)

        recycling.input = __builtins__.input  # Replace mock with original input


    def test_main(self):
        example_data = ['4', '1', '3', '2', '3']
        mock_input = Mock(side_effect=example_data)
        recycling.input = mock_input

        recycling.main()  # verify program doesn't crash :) Could also test that it's printing correct data with a mock print function.
        recycling.input = __builtins__.input  # Replace mock with original input




if __name__ == '__main__':
    unittest.main()
