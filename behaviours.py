# Help out by adding to/ improving these lists!!!
from waterloo_api_data import connections

PHRASE_TYPES = ['GREETING', 'FUN', 'ABOUT_SELF', 'MENU', 'WEATHER']

class KeyWords:
    """ Contains keywords/ phrases for the bot.
        Since the input similarity check gets divided by how many words were messaged,
        any number of words in the greeting phrase can still be matched.
    """
    def __init__(self):
        self.GREETING = [
            ["hello", "how", "are", "you", "doing"],
            ["hey", "what 's", "up"],
            ["hi", "how 's", "it", "going"],  # Note: words with 's must have a space before due to TextBlob.tags
            ["yo", "what 's", "going", "on"],
            ["how 's", "your", "day", "going"],
            ["good", "morning", "afternoon", "night", "evening"],  # will likely type good {something}
            ["nice", "to", "meet", "you"],
            ["hey", "how", "goes", "it"]
        ]

        self.FUN = [
            ["thanks", "mister", "goose"],
            ["who", "do", "you", "miss", "the", "most"]
        ]

        self.ABOUT_SELF = [
            ["Who", "are", "you"],
            ["what", "is", "your", "name"]
        ]

        self.MENU = [
            ["what 's", "on", "the", "menu", "at", "v1"]
        ]

        self.WEATHER = [
            ["what 's", "the", "current", "weather", "in", "waterloo"]
        ]


class Responses:
    """ Contains simple responses for the bot"""
    def __init__(self):
        self.HELP = "Try asking: " \
                    "What is the current weather in Waterloo? " \
                    "What is on the v1 menu?"

        self.GREETING = ["what's up?",
                         "hey!",
                         "Today is a great day, how are you?"
                         ]

        self.FUN = ["np",
                    "harambe ;-;"
                    ]

        self.ABOUT_SELF = ["I do and feel nothing, I'm a robot :)",
                           "My favourite thing is being Sexxi",
                           "My name is Goose"
                           ]

        self.MENU = ["The v1 menu contains: "]  # Will need to look up

        weather = connections.get_temperature()
        self.WEATHER = ["The current weather in Waterloo is: " + weather[0]]
        if weather[1]:  # There is rain
            self.WEATHER[0] += " and some rain"
        else:
            self.WEATHER[0] += " and no rain"

        self.UNSURE = ["Try telling me something else",
                       "Sorry, I didn't quite get that",
                       "Can you rephrase that?"
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
            "hbu": "how about you",
            "thank": "thanks",
            "mr": "mister"
            }
