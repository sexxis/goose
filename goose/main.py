from response.response import *
import operator
import random

__author__ = "Waterloo SE'XXI"

bot = SexxiBot()


def run_bot(user_input, start):
    if start:
        bot.response = "Hello there! Have a chat with me or say 'help' to see available commands :)"
        return bot.response

    bot.user_input = user_input

    # fix_typos:    Fix any user typos and slang
    # check_phrase_similarity:  Check user's input similarity to all key phrases
    # create_response:  If all key phrases fail, we gotta actually make a new sentence
    for method in ['fix_typos', 'help_check', 'check_phrase_similarity', 'create_response']:
        if operator.methodcaller(method)(bot):
            return bot.response
    return random.choice(responses.UNSURE)  # If no response can be created


# For testing purposes
def test():
    print run_bot(user_input=None, start=True)
    while 1:
        print run_bot(user_input=raw_input("Enter a message: "), start=False)

if __name__ == '__main__':
    try:
        test()
    except KeyboardInterrupt:  # No need for an error when stopping the program during testing
        pass
