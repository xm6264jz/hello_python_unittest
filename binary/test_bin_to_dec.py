import unittest
import bin_to_dec

class TestBinaryToDecimal(unittest.TestCase):

    def test_binary_decimal_conversion_with_binary_numbers(self):

        # Python's bin method does the conversion from binary to decimal

        # Loops are helpful - test a range of numbers
        for d in range(100):

            binary = bin(d)  # in the format '0b10101'
            binary = binary[2:]  # Remove the inital '0b'

            dec_output = bin_to_dec.decimal(binary)

            self.assertEqual(d, dec_output)

        # Lets test some larger numbers too
        # Some 'round numbers' and some other large numbers

        test_vals = [4000, 4001, 4002, 1024, 1099511627776, 1099511627777, 1099511627775]

        for d in test_vals:
            binary = bin(d)  # in the format '0b10101'
            binary = binary[2:]  # Remove the inital '0b'

            dec_output = bin_to_dec.decimal(binary)

            self.assertEqual(d, dec_output)


        # And test with some actual strings
        test_bin_str = [ '101010', '1111', '000111', '0', '1']
        expected_dec = [ 42, 15, 7, 0, 1]

        for binary_input, expected_dec_output in zip( test_bin_str, expected_dec) :
            dec = bin_to_dec.decimal(binary_input)
            self.assertEqual(dec, expected_dec_output)


    def test_binary_decimal_conversion_with_invalid_input(self):

        # Verify a value error is raised with strings that are not made entirely of 0 and 1.

        valid = '010101'
        valid2 = '1111111'

        invalid = [ '123456', '101010012', 'abc', '@#$%$%^%^&']
        for invalid_input in invalid:
            with self.assertRaises(ValueError):
                bin_to_dec.decimal(invalid_input)


if __name__ == '__main__':
    unittest.main()
