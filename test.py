import unittest
from main import *
import unittest.mock


class testrandom(unittest.TestCase):

    def test_random_byte_output_is_an_int(self):
        #create an
        rand_byte = RandomByte("D")
        self.assertEqual(type(rand_byte()), int)

        rand_byte = RandomByte("S")
        self.assertEqual(type(rand_byte()), int)

        rand_byte = RandomByte("W")
        self.assertEqual(type(rand_byte()), int)


class MockRandInt:

    def __init__(self, *args):
        self.fake_random_value = None

    def set_return_value(self, fake_random_value):
        self.fake_random_value = fake_random_value

    def __call__(self, *args, **kwargs):
        if self.fake_random_value is None:
            raise Exception("MockRandInt output must be set with set_return_value")
        return self.fake_random_value

class MockRandChoice:

    def __init__(self):
        self.fake_choice_index = None

    def set_fake_choice_index(self, i):
        self.fake_choice_index = i

    def __call__(self, choices):
        return choices[self.fake_choice_index]


def extract_mock_print_text(mocked_print):
    try:
        return mocked_print.mock_calls[0][1][0]
    except IndexError:
        raise Exception("No printed text found")


class TestQuestions(unittest.TestCase):

    def test_bin_question(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            none_return_value = bin_question(3)
            self.assertIsNone(none_return_value)

            extracted_text = extract_mock_print_text(mocked_print)
            self.assertTrue("Binary" in extracted_text)
            self.assertTrue(" 11" in extracted_text)

    def test_dec_question(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            none_return_value = dec_question(25)
            self.assertIsNone(none_return_value)

            extracted_text = extract_mock_print_text(mocked_print)
            self.assertTrue("Decimal" in extracted_text)
            self.assertTrue(" 25" in extracted_text)


class TestBin(unittest.TestCase):

    def test_correct_binary_answer(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            with unittest.mock.patch('builtins.input', return_value="101") as mocked_input:
                bin_user_answer(5)
                print_text = extract_mock_print_text(mocked_print)
                self.assertIn("Correct", print_text)
                self.assertNotIn("Incorrect", print_text)

    def test_incorrect_binary_answer(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            with unittest.mock.patch('builtins.input', return_value="111") as mocked_input:
                bin_user_answer(8)
                print_text = extract_mock_print_text(mocked_print)
                self.assertIn("Incorrect", print_text)


class TestDec(unittest.TestCase):

    def test_correct_decimal_answer(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            with unittest.mock.patch('builtins.input', return_value="105") as mocked_input:
                dec_user_answer(105)
                print_text = extract_mock_print_text(mocked_print)
                self.assertIn("Correct", print_text)
                self.assertNotIn("Incorrect", print_text)

    def test_incorrect_decimal_answer(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            with unittest.mock.patch('builtins.input', return_value="101") as mocked_input:
                dec_user_answer(7)
                print_text = extract_mock_print_text(mocked_print)
                self.assertIn("Incorrect", print_text)


class TestHex(unittest.TestCase):

    def test_correct_hexadecimal_answer(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            with unittest.mock.patch('builtins.input', return_value="b") as mocked_input:
                hex_user_answer(11)
                print_text = extract_mock_print_text(mocked_print)
                self.assertIn("Correct", print_text)
                self.assertNotIn("Incorrect", print_text)

class TestCodes(unittest.TestCase):

    def test_import(self):
        self.assertTrue(hex_format)


if __name__ == "__main__":
    unittest.main()


