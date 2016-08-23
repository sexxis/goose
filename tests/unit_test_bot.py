import unittest
from test_phrases import *
from goose.response.response import responses
from goose.response import constants
from goose.main import run_bot

phrase_tests = TestPhrases()
template_tests = TestTemplates()


class TestBotResponses(unittest.TestCase):
    def test_help_response(self):
        self.assertEqual(run_bot('help', start=False), responses.HELP)

    def test_basic_responses(self):
        error = False
        for phrase_type in constants.PHRASE_TYPES:
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
                        error = True
        if error:  # May as well fail the test if a case does not pass
            raise AssertionError

    def test_template_responses(self):
        error = False
        for case_num in range(template_tests.num_cases):
            case_num = str(case_num+1)
            try:
                self.assertEqual(run_bot(user_input=getattr(template_tests, 'case' + case_num)[0], start=False),
                                 getattr(template_tests, 'case' + case_num)[1])
            except AssertionError:
                print case_num
                error = True
        if error:
            raise AssertionError


if __name__ == '__main__':
    unittest.main(exit=False)
