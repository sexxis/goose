# Help out by adding to/ improving these lists!!!


class KeyWords:
    """ Contains keywords/ phrases for the bot.
        Since the input similarity check gets divided by how many words were messaged,
        any number of words in the greeting phrase can still be matched.
    """
    def __init__(self):
        self.GREETING_PHRASES = [
            ["hello", "how", "are", "you", "doing"],
            ["hey", "what's", "up"],
            ["hi", "how", "is", "it", "going"],
            ["yo", "what's", "going", "on"],
            ["how", "is", "your", "day", "going"],
            ["good", "morning", "afternoon", "night", "evening"],  # will likely type good {something}
            ["nice", "to", "meet", "you"],
            ["hey", "how", "goes", "it"]
        ]

        self.ABOUT_SELF = [
            ["Who", "are", "you"],
            ["what", "is", "your", "name"]
        ]

        self.MENU_PHRASES = [
            ["what", "is", "on", "the", "menu", "at", "v1"]
        ]


class Responses:
    """ Contains simple responses for the bot"""
    def __init__(self):
        self.GREETING_RESPONSES = ["what's up?",
                                   "hey!",
                                   "Today is a great day, how are you?"
                                   ]

        self.SELF_RESPONSES = ["I do and feel nothing, I'm a robot :)",
                               "My favourite thing is being Sexxi",
                               "My name is Goose"]

        self.MENU_RESPONSES = list()  # Will need to look up

        self.UNSURE_RESPONSES = ["Ahhh ya got me, I'm not sure what to say :3"]  # I'll make sure this doesn't happen


# Don't check these when assessing phrase similarity
unimportant_words = [
    "it",
    "is",
]

# Used for fixing user typos or laziness
slang_typo_dict = {
            "ngl": "not going to lie",
            "sup": "what's up",
            "i": "I",
            "im": "I'm",
            "i'm": "I'm",
            "u": "you",
            "how's": "how is",
            "wasup": "what's up",
            "wadup": "what's up",
            "wats": "what's",
            "wat": "what",
            "wut": "what",
            "hbu": "how about you"
            }
