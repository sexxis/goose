class TestPhrases(object):
    def __init__(self):
        self.GREETING = ["hello",
                         "hey how are you"
                         # Add more tests for each phrase type
                         ]

        self.FUN = ["thanks mr goose",

                    ]

        self.ABOUT_SELF = ["what's your name?",
                           "who are you"

                           ]

        self.MENU = ["What's on the v1 menu"

                     ]

        self.WEATHER = ["what's the current weather in waterloo?",
                        "What's waterloo's current weather?"

                        ]


class TestTemplates(object):
    def __init__(self):
        self.num_cases = 2
        self.case1 = ["I like pizza",
                      "pizza sounds interesting"]

        self.case2 = ["i love my computer",
                      "computer sounds interesting"]
