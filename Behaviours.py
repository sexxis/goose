# Help out by adding to/ improving these lists!!!


class KeyWords:
    """ Contains keywords/ phrases for the bot.
        Since the input similarity check gets divided by how many words were messaged,
        any number of words in the greeting phrase can still be matched.
    """
    def __init__(self):
        self.GREETING_PHRASES = [
            ["hello", "how", "are", "you", "doing"],
            ["hey", "what 's", "up"],
            ["hi", "how 's", "it", "going"],  # Note: words with 's must have a space before due to TextBlob.tags
            ["yo", "what 's", "going", "on"],
            ["how 's", "your", "day", "going"],
            ["good", "morning", "afternoon", "night", "evening"],  # will likely type good {something}
            ["nice", "to", "meet", "you"],
            ["hey", "how", "goes", "it"]
        ]

        self.ABOUT_SELF = [
            ["Who", "are", "you"],
            ["what", "is", "your", "name"]
        ]

        self.MENU_PHRASES = [
            ["what 's", "on", "the", "menu", "at", "v1"]
        ]

        self.WEATHER_PHRASES = [
            ["what 's", "the", "current", "weather", "in", "waterloo"]
        ]


class Responses:
    """ Contains simple responses for the bot"""
    def __init__(self):
        self.HELP_RESPONSE = "Try asking: " \
                             "What is the current weather in Waterloo? " \
                             "What is on the v1 menu?"

        self.GREETING_RESPONSES = ["what's up?",
                                   "hey!",
                                   "Today is a great day, how are you?"
                                   ]

        self.SELF_RESPONSES = ["I do and feel nothing, I'm a robot :)",
                               "My favourite thing is being Sexxi",
                               "My name is Goose"
                               ]

        self.MENU_RESPONSES = ["The v1 menu contains: "]  # Will need to look up

        self.WEATHER_RESPONSES = ["The current weather in Waterloo is: ",
                                  " and no rain",
                                  " and some rain",
                                  " and heavy rain"
                                  ]

        self.UNSURE_RESPONSES = ["Try telling me something else",
                                 "Sorry, I didn't quite get that",
                                 "Can you rephrase that?",
                                 ]


# Don't check these when assessing phrase similarity
unimportant_words = [
    "it",
    "is",
    "to"
    ]

# Used for fixing user typos or laziness
slang_typo_dict = {
            "ngl": "not going to lie",
            "sup": "what's up",
            "i": "I",
            "im": "I'm",
            "i'm": "I'm",
            "u": "you",
            "wasup": "what's up",
            "wadup": "what's up",
            "wats": "what's",
            "wat": "what",
            "wut": "what",
            "hbu": "how about you"
            }
