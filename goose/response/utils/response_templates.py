from jinja2 import Template


def determine_response_type():
    # Will determine what response template to choose from
    return 'name_is'  # temporarily return this for testing purposes


class ResponseTemplates(object):
    def __init__(self, noun, pronoun, verb, adj, prep):
        self.response = str()
        self.parts = {'noun': noun, 'verb': verb, 'adj': adj, 'pronoun': pronoun, 'prep': prep}

        # Will have a large amount of templates
        self.name_is = Template('Hello {{noun}}!')
        self.like_noun = Template('I like {{noun}}')

    def respond(self, resp_type=determine_response_type()):
        # Will add in any found parts to the determined response type
        return getattr(self, resp_type).render(noun=self.parts['noun'],
                                               verb=self.parts['verb'],
                                               adj=self.parts['adj'],
                                               pronoun=self.parts['pronoun'],
                                               prep=self.parts['prep'])


# Tests
if __name__ == '__main__':
    test = ResponseTemplates(noun="Dylan", pronoun=None, verb=None, adj=None, prep=None)
    print test.respond('name_is')  # Prints "Hello Dylan!"
