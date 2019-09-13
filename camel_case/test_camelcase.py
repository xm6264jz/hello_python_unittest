import unittest
from unittest.mock import patch
import camel

class TestCamelCase(unittest.TestCase):

    def test_capitalize(self):

        input_words = ['lum', 'LUM', 'lUMM', 'LUm']
        capitalized = 'Lum'

        for word in input_words:
            self.assertEqual(capitalized, camel.capitalize(word))




def test_lower(self):

        input_words = ['lum', 'LUM', 'lUM', 'LUm']
        lower = 'lum'

        for word in input_words:
            self.assertEqual(lower, camel.lowercase(word))


    def test_camel_case(self):

        input_and_expected_outputs = {
            '' : '' ,
            'bye' : 'bye',
            'Bye' : 'bye',
            'Bye bye' : 'byeBye',
            'BYE BYE' : 'byeBye',
            'bYE BYE' : 'byeBye',

        }

        for input_val in input_and_expected_outputs.keys():
            # assertEqual(expected, actual)
            self.assertEqual(input_and_expected_outputs[input_val], camel.camel_case(input_val))



    def test_input_and_output(self):

        with patch('builtins.input', return_value='This IS a SENTenCE'):

            # And, patch the output
            with patch('builtins.print') as mock_print:

                camel.main()
                mock_print.assert_called_with('thisIsASentence')



if __name__ == '__main__':
    unittest.main()