# STILL NEEDS LOTS OF WORK! :D


def craft_response(noun, pronoun, verb, adj):
    """ Creates a response based on the user's input """
    resp = list()

    if pronoun:
        resp.append(pronoun)

    if verb:
        verb_word = verb[0]
        if verb == "are":
            resp.append("am")

        else:
            if verb_word in ('be', 'am', 'is', "'m"):
                if pronoun.lower() == 'you':
                    resp.append(verb_word)

    if adj:
        resp.append(adj)

    if noun:
        pronoun = "an" if vowel_start(noun) else "a"
        resp.append(pronoun + " " + noun)

    return " ".join(resp)


def vowel_start(word):
    return True if word[0] in "aeiou" else False
