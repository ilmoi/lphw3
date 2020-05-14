"""
iterate through tuples
access tuple[0]
if tuple 0 is noun or direction = keep for subject
if tuple 0 is verb = keep for verb
else discard
associate verb with noun that comes after it

look for verb first
then look for either noun or direction as subject

"""

class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subj, verb, obj):
        self.subj = subj[1]
        self.verb = verb[1]
        self.obj = obj[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0) #without 0 here you're returning last not first
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)
        # key is - we're returning the word but we're not storing it
        # so really just the pop

def parse_verb(word_list):
    # print(word_list)
    skip(word_list, 'stop')
    # print(word_list)
    if peek(word_list) == 'verb':
        # print('hooray')
        # print(match(word_list, 'verb'),'1234')
        return match(word_list, 'verb')
    else:
        raise ParserError('Expecting a verb next')

def parse_object(word_list):
    skip(word_list, 'stop')
    if peek(word_list) == 'noun':
        return match(word_list, 'noun')
    elif peek(word_list) == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError('Expecting a noun or direction next.')

def parse_subject(word_list):
    skip(word_list, 'stop')
    if peek(word_list) == 'noun':
        return match(word_list, 'noun')
    elif peek(word_list) == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError('Expecting a noun or a verb.')

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    # print(subj)
    verb = parse_verb(word_list)
    # print(verb)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)

if __name__ == "__main__":
    import lexicon
    s = 'run north'
    x = lexicon.scan(s)
    print(x)
    y = parse_sentence(x)
    print(y.subj)
    print(y.verb)
    print(y.obj)
    print(y)
