""" Use POS tags to find useful sentence parts"""
POS_NOUN = "NN"
POS_PRONOUN = "PRP"
POS_VERB = "VB"
POS_ADJ = "JJ"
POS_PREP = "IN"


def pos_tags(text):
    noun, pronoun, verb, adj, prep = None, None, None, None, None
    index = int()

    for word, pos in text:
        # print word, pos

        if pos == POS_NOUN:
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

        elif pos == POS_PREP and not prep:
            prep = word

        index += 1

    return noun, pronoun, verb, adj, prep
