from textblob import TextBlob
from generate_response import format_response, check_pos_tags
from stringscore import liquidmetal
import behaviours
import random
import operator
import sys

__author__ = "Waterloo SE'XXI"


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


sys.stdout = Unbuffered(sys.stdout)

keywords = behaviours.KeyWords()
responses = behaviours.Responses()


class SexxiBot:
    """ Main ChatBot class containing methods to check for specific inputs and create an appropriate response """
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
            if words[part] in behaviours.slang_typo_dict.keys():
                words[part] = behaviours.slang_typo_dict[words[part]]
        self.user_input = ' '.join(words)
        return False

    def help_check(self):
        if self.user_input.lower() == "help":
            self.response = responses.HELP
            return True  # Stop, as we know what category of input we're dealing with
        return False  # User didn't ask for help, move on to greeting_check

    def check_phrase_similarity(self):
        self.user_input = TextBlob(self.user_input.lower()).tags  # Do this once; greeting_check must run first
        self.input_len = len(self.user_input)  # Find this once too; will be used for scoring
        for phrase_type in behaviours.PHRASE_TYPES:
            for phrase in getattr(keywords, phrase_type):
                score = float()
                for word in self.user_input:
                    for n in phrase:
                        if word and n not in behaviours.unimportant_words:
                            score += liquidmetal.score(n, word[0]) / self.input_len
                if score >= 0.7:  # Could be increased/ decreased through testing to find more optimal value
                    self.response = random.choice(getattr(responses, phrase_type))
                    return True
        return False

    def create_response(self):  # Not really working yet
        # Craft a response based on user's message
        noun, pronoun, verb, adj, prep, text_len = check_pos_tags.pos_tags(self.user_input)
        self.response = format_response.craft_response(noun, pronoun, verb, adj, prep, text_len)
        print self.response
        return False if self.response == ' ' else True


bot = SexxiBot()  # Instantiate the bot


def run_bot(user_message, start):
    if start:
        bot.response = "Hello there! Have a chat with me or say 'help' to see available commands :)"
        return bot.response

    bot.user_input = raw_input(user_message)

    # fix_typos:    Fix any user typos and slang
    # check_phrase_similarity:  Check user's input similarity to all key phrases
    # create_response:  If all key phrases fail, we gotta actually make a new sentence
    for method in ['fix_typos', 'help_check', 'check_phrase_similarity', 'create_response']:
        if operator.methodcaller(method)(bot):
            return bot.response
    return random.choice(responses.UNSURE)  # If no response can be created


# For testing purposes
def main():
    print run_bot("Enter a message: ", start=True)
    while 1:
        print run_bot("Enter a message: ", start=False)


# Make sure it's only when we're running this file directly
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
