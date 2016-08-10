from textblob import TextBlob
from Generate_Response import Format_Response
from Generate_Response import Check_POSTags
import Behaviours
import random

__author__ = "Waterloo SE'XXI"

keywords = Behaviours.KeyWords()
responses = Behaviours.Responses()


class SexxiBot:
    """ Main ChatBot class containing methods to check for specific inputs and create an appropriate response """
    def __init__(self):
        self.user_input = str()
        self.response = str()

    def fix_typos(self):
        # Fix lazy user typos, or slang
        slang_dict = {"ngl": "not going to lie", "sup": "what's up"}
        words = self.user_input.split()
        for part in range(len(words)):
            if words[part] == 'i':
                words[part] = 'I'
            elif words[part] == "i'm":
                words[part] = "I'm"

            if words[part] in slang_dict.keys():
                words[part] = slang_dict[words[part]]

        self.user_input = ' '.join(words)

    def greeting_check(self):
        # Check to see if someone is just saying hi
        user_text = (self.user_input.lower()).split()
        for word in user_text:
            if word in keywords.GREETING_KEYWORDS:
                self.response = random.choice(responses.GREETING_RESPONSES)
                return True
        return False

    def create_response(self):
        # Craft a response based on user's message
        self.user_input = TextBlob(self.user_input)
        noun, pronoun, verb, adj = Check_POSTags.pos_tags(self.user_input.tags)
        self.response = Format_Response.craft_response(noun, pronoun, verb, adj)


# For Testing Purposes
if __name__ == '__main__':
    bot = SexxiBot()

    bot.user_input = "You are cool"
    bot.fix_typos()
    print bot.user_input

    if not bot.greeting_check():
        bot.create_response()

    print bot.response  # Responds with "I am cool"
