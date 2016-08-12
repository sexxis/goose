# Is used when a key response is not triggered.
import random


def craft_response(noun, pronoun, verb, adj, prep, text_len):
    """ Creates a response based on the user's input """
    print noun, pronoun, verb, adj, prep, text_len
    resp = list()
    verb_last = False

    if pronoun:
        resp.append(pronoun)

    if verb:
        if verb[0] == "are":
            resp.append("am")

        elif verb[1] == text_len - 1:   # if the verb is at the end of the sentence
            verb_last = True
        else:
            resp.append(verb[0])

        if resp == ['I']:
            resp.append("am")

    if adj:
        resp.append(adj)

    if prep:
        resp.append(prep)

    if noun:
        pronoun = "an" if vowel_start(noun) else "a"
            #resp.append(pronoun + " " + noun)
        resp.append(noun)

    if verb_last:
        resp.append(verb[0])

    return " ".join(resp)


def vowel_start(word):
    return True if word[0] in "aeiou" else False
