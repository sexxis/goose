""" Use POS tags to find useful sentence parts"""
POS_NOUN = "NN"
POS_PRONOUN = "PRP"
POS_VERB = "VB"
POS_ADJ = "JJ"


def pos_tags(text):
    noun = False
    pronoun = False
    verb = False
    adj = False

    for word, pos in text:
        if noun and pronoun and verb and adj:
            break

        elif pos == POS_NOUN and not noun:
            noun = word

        elif pos == POS_PRONOUN and not pronoun:
            if word.lower() == "you":
                pronoun = 'I'
            elif word.lower() == 'I':
                pronoun = "you"

        elif pos.startswith(POS_VERB) and not verb:
            verb = word

        elif pos == POS_ADJ and not adj:
            adj = word

    return noun, pronoun, verb, adj
