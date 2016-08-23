from textblob import TextBlob
from stringscore import liquidmetal
from utils import check_pos_tags
from utils.response_templates import ResponseTemplates
from constants import *
import random
import sys


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


sys.stdout = Unbuffered(sys.stdout)

keywords = KeyWords()
responses = Responses()


class SexxiBot(object):
    """ Main ChatBot class to take in user input and return an appropriate response.

    Contains methods: fix_typos, to correct any user's typos;
    help_check, to check if the user has asked for 'help' (a list of possible commands);
    check_phrase_similarity, to compare user inputs to keywords to generate basic responses;
    create_response, to generate a new response based on the users input.
    """

    def __init__(self):
        self.user_input = str()
        self.input_len = int()
        self.response = str()

    def fix_typos(self):
        self.user_input = TextBlob(self.user_input.lower()).tags
        # Fix lazy user typos, or slang
        words = list()
        for i in self.user_input:
            words.append(i[0])

        for part in range(len(words)):
            if words[part] in slang_typo_dict.keys():
                words[part] = slang_typo_dict[words[part]]
        self.user_input = ' '.join(words)
        return False  # Returns false to move on to help_check

    def help_check(self):
        if self.user_input.lower() == "help":
            self.response = responses.HELP
            return True
        return False  # User didn't ask for help, move on to check_phrase_similarity

    def check_phrase_similarity(self):
        self.user_input = TextBlob(self.user_input.lower()).tags
        self.input_len = len(self.user_input)
        for phrase_type in PHRASE_TYPES:
            for phrase in getattr(keywords, phrase_type):
                score = float()
                for word in self.user_input:
                    for n in phrase:
                        if word and n not in unimportant_words:
                            score += liquidmetal.score(n, word[0]) / self.input_len
                if score >= 0.7:  # Could be increased/ decreased through testing to find more optimal value
                    self.response = random.choice(getattr(responses, phrase_type))
                    return True
        return False

    def create_response(self):
        # Create a template response based on parts in user_input
        noun, pronoun, verb, adj, prep = check_pos_tags.pos_tags(self.user_input)
        self.response = ResponseTemplates(noun=noun, pronoun=pronoun, verb=verb, adj=adj, prep=prep).respond()
        return False if self.response == str() else True
