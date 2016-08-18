import unittest
from test_phrases import *
from sexxi_bot import *

phrase_tests = TestPhrases()


class TestBotResponses(unittest.TestCase):
    def test_help_response(self):
        self.assertEqual(run_bot('help', start=False), responses.HELP)

    def test_basic_responses(self):
        for phrase_type in behaviours.PHRASE_TYPES:
            phrase_num = 1
            for phrase in getattr(phrase_tests, phrase_type):
                    test_case = False
                    if run_bot(phrase, start=False) in getattr(responses, phrase_type):
                        test_case = True
                    try:
                        self.assertTrue(test_case)
                        phrase_num += 1
                    except AssertionError:  # except to still check over all phrase types
                        print phrase_type, phrase_num  # print out each input that triggered an incorrect response


if __name__ == '__main__':
    unittest.main(exit=False)
