import unittest
from unittest.mock import Mock
import camel

class TestCamelCase(unittest.TestCase):

    def test_capitalize(self):

        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        capitalized = 'Abc'

        for word in input_words:
            self.assertEqual(camel.capitalize(word), capitalized)


    def test_lower(self):
        # this isn't really needed, since we can assume that Python's library functions work correctly :)
        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        lower = 'abc'

        for word in input_words:
            self.assertEqual(camel.lowercase(word), lower)


    def test_camel_case(self):

        input_and_expected_outputs = {
            '' : '' ,
            'hello' : 'hello',
            'Hello' : 'hello',
            'Hello world' : 'helloWorld',
            'HELLO WORLD' : 'helloWorld',
            'hELLO wORLD' : 'helloWorld',
            'this is a sentence' : 'thisIsASentence',
            'Here is a long sentence with many words' : 'hereIsALongSentenceWithManyWords'
        }

        for input in input_and_expected_outputs.keys():
            self.assertEqual(camel.camel_case(input), input_and_expected_outputs[input])


    def test_input_and_output(self):
        mock_input = Mock(return_value='This IS another SENTenCE')
        camel.input = mock_input
        mock_print = Mock()
        camel.print = mock_print

        camel.main()

        mock_print.assert_called_with('thisIsAnotherSentence')


if __name__ == '__main__':
    unittest.main()
