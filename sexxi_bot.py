from textblob import TextBlob
from generate_response import format_response
from generate_response import check_pos_tags
from stringscore import liquidmetal
import behaviours
import random

__author__ = "Waterloo SE'XXI"

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
        self.input_len = len(self.user_input)                       # This too; so you don't need to keep checking

        # Fix lazy user typos, or slang
        words = list()
        for i in self.user_input:
            words.append(i[0])

        for part in range(len(words)):
            if words[part] in behaviours.slang_typo_dict.keys():
                words[part] = behaviours.slang_typo_dict[words[part]]
        self.user_input = ' '.join(words)

    def help_check(self):
        if self.user_input.lower() == "help":
            # Will list possible commands/ etc
            return True
        return False

    def greeting_check(self):
        self.user_input = TextBlob(self.user_input.lower()).tags  # Do this once; greeting_check must run first
        for phrase in keywords.GREETING_PHRASES:
            score = float(0)
            for word in self.user_input:
                for n in phrase:
                    if word and n not in behaviours.unimportant_words:
                        score += liquidmetal.score(n, word[0]) / self.input_len
            if score >= 0.7:    # Could be increased/ decreased through testing to find more optimal value
                self.response = random.choice(responses.GREETING_RESPONSES)
                return True
        return False

    def asked_about_self(self):
        for phrase in keywords.ABOUT_SELF:
            score = float()
            for word in self.user_input:
                for n in phrase:
                    if word and n not in behaviours.unimportant_words:
                        score += liquidmetal.score(n, word[0]) / self.input_len
            print score
            if score >= 0.7:
                self.response = random.choice(responses.SELF_RESPONSES)
                return True
        return False

    def menu_check(self):
        for phrase in keywords.ABOUT_SELF:
            score = float()
            for word in self.user_input:
                for n in phrase:
                    if word and n not in behaviours.unimportant_words:
                        score += liquidmetal.score(n, word[0]) / self.input_len
            if score >= 0.7:
                self.response = random.choice(responses.SELF_RESPONSES)
                return True
        return False

    def create_response(self):  # Not really working yet
        # Craft a response based on user's message
        noun, pronoun, verb, adj, prep, text_len = check_pos_tags.pos_tags(self.user_input)
        self.response = format_response.craft_response(noun, pronoun, verb, adj, prep, text_len)
        return False


# For Testing Purposes
if __name__ == '__main__':
    bot = SexxiBot()
    bot.user_input = "What foods do you like"  # Would receive input from user of course

    bot.fix_typos()

    print bot.user_input

    if not bot.help_check():
        if not bot.greeting_check():
            if not bot.asked_about_self():
                if not bot.menu_check():
                    bot.create_response()  # If all key phrases fail, we gotta actually make a new sentence :)

    print "Response:", bot.response
