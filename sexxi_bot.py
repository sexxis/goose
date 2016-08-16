from textblob import TextBlob
from generate_response import format_response
from generate_response import check_pos_tags
from waterloo_api_data import connections
from stringscore import liquidmetal
import behaviours
import random
import operator

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
            self.response = responses.HELP_RESPONSE
            return True  # Stop, as we know what category of input we're dealing with
        return False  # User didn't ask for help, move on to greeting_check

    def greeting_check(self):
        self.user_input = self.user_input.tags  # Do this once; greeting_check must run first
        self.input_len = len(self.user_input)                     # Find this once too; will be used for scoring
        for phrase in keywords.GREETING_PHRASES:
            score = float()
            for word in self.user_input:
                for n in phrase:
                    if word and n not in behaviours.unimportant_words:
                        score += liquidmetal.score(n, word[0]) / self.input_len
            if score >= 0.7:    # Could be increased/ decreased through testing to find more optimal value
                self.response = random.choice(responses.GREETING_RESPONSES)
                return True
        return False

    def fun_check(self):
        #disclaimer: i don't know any NLP so i'm just matching stuff like "thank mr goose"
        self.user_input = TextBlob(self.user_input.lower())
        for phrase in keywords.FUN_PHRASES:
            if phrase == self.user_input.words:
                n = [i for i, x in enumerate(keywords.FUN_PHRASES) if x == phrase][0]
                self.response = responses.FUN_RESPONSES[n]
                return True
        return False

    def asked_about_self(self):
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

    def menu_check(self):
        for phrase in keywords.MENU_PHRASES:
            score = float()
            for word in self.user_input:
                for n in phrase:
                    if word and n not in behaviours.unimportant_words:
                        score += liquidmetal.score(n, word[0]) / self.input_len
            if score >= 0.7:
                self.response = responses.MENU_RESPONSES[0]
                return True
        return False

    def weather_check(self):
        for phrase in keywords.WEATHER_PHRASES:
            score = float()
            for word in self.user_input:
                for n in phrase:
                    if word and n not in behaviours.unimportant_words:
                        score += liquidmetal.score(n, word[0]) / self.input_len
            if score >= 0.7:
                temp = connections.get_temperature()
                self.response = responses.WEATHER_RESPONSES[0] + temp[0]
                if temp[1]:  # There is rain
                    self.response += responses.WEATHER_RESPONSES[2]
                else:
                    self.response += responses.WEATHER_RESPONSES[1]
                return True
        return False

    def create_response(self):  # Not really working yet
        # Craft a response based on user's message
        noun, pronoun, verb, adj, prep, text_len = check_pos_tags.pos_tags(self.user_input)
        self.response = format_response.craft_response(noun, pronoun, verb, adj, prep, text_len)
        print self.response
        return False if self.response == ' ' else True


def run_bot(user_message, start):
    bot = SexxiBot()
    if start:
        bot.response = "Hello there! Have a chat with me or say 'help' to see available commands :)"
        return bot.response

    bot.user_input = user_message
    bot.fix_typos()
    
    #fun_check: do fun_check before greeting_check because we are looking for specific things
    #create_response:  If all key phrases fail, we gotta actually make a new sentence
    for method in ['help_check','fun_check','greeting_check','asked_about_self','menu_check','weather_check','create_response']:
      if operator.methodcaller(method)(bot):
        return bot.responseoperator.methodcaller(method)
    return responses.UNSURE_RESPONSES[0]; # If no response can be created


# For testing purposes
def main():
    start = True
    while 1:
        print run_bot(raw_input("Enter a message: "), start)
        start = False


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
