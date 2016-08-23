from jinja2 import Template


class ResponseTypeNotFoundError(Exception):
    pass


class ResponseTemplates(object):
    def __init__(self, noun, pronoun, verb, adj, prep):
        self.response = str()
        self.parts = {'noun': noun, 'verb': verb, 'adj': adj, 'pronoun': pronoun, 'prep': prep}

        # Will have a large amount of templates
        self.name_is = Template('Hello {{adj}}!')  # the name will be considered an adj.
        self.like_noun = Template('{{noun}} sounds interesting')

    def determine_response_type(self):
        if self.parts['noun'] == 'name' and self.parts['adj']:
            return 'name_is'
        elif self.parts['verb'] in ['like', 'love', 'want'] and self.parts['noun']:
            return 'like_noun'

        else:
            raise ResponseTypeNotFoundError

    def respond(self):
        try:    # if a response type is not found, the return will not work; raise an error
            resp_type = self.determine_response_type()
            # Will add in any found parts to the determined response type
            return getattr(self, resp_type).render(noun=self.parts['noun'],
                                                   verb=self.parts['verb'],
                                                   adj=self.parts['adj'],
                                                   pronoun=self.parts['pronoun'],
                                                   prep=self.parts['prep'])

        except ResponseTypeNotFoundError:
            return self.response
