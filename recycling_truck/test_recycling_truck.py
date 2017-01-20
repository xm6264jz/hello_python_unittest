import unittest
from unittest.mock import Mock, patch

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

        '''
        Create a patch to replace the built in input function with a mock.
        The mock is called mock_input, and we can change the way it behaves, e.g. provide
        our desired return values. So when the code calls input(), instead of
        calling the built-in input function, it will call the mock_input mock function,
        which doesn't do anything except for returning the values provided in the
        list of side_effect values - the first time it is called, it returns the first
        side_effect value (1), second time it will return the second value, (3) etc...

        '''

        with patch('builtins.input') as mock_input:
            mock_input.side_effect = example_data
            self.assertEqual(recycling.get_crate_quantities(6), example_data)


    def test_int_input(self):

        # Test with some invalid input

        with patch('builtins.input') as mock_input:
            example_invalid_inputs = ['-2', '-1000', 'abc', '123abc', '3']  # Put a valid input at the end or the function will never return
            mock_input.side_effect = example_invalid_inputs
            self.assertEqual(recycling.positive_int_input('example question'), 3) #Ultimately, should return the valid value at the end of the list. 


        with patch('builtins.input') as mock_input:
            example_valid_inputs = [ '0', '13', '1', '100000000']
            mock_input.side_effect = example_valid_inputs

            self.assertEqual(recycling.positive_int_input('example question'), 0)
            self.assertEqual(recycling.positive_int_input('example question'), 13)
            self.assertEqual(recycling.positive_int_input('example question'), 1)
            self.assertEqual(recycling.positive_int_input('example question'), 100000000)



    def test_main(self):

        with patch('builtins.input') as mock_input:

            example_data = ['4', '1', '3', '2', '3']
            mock_input.side_effect = example_data
            recycling.input = mock_input

            recycling.main()  # verify program doesn't crash :) Could also test that it's printing correct data with a mock print function.




if __name__ == '__main__':
    unittest.main()
