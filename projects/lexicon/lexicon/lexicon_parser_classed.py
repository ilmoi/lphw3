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

    #don't need to make a classmethod since not calling any cls variables
    def peek(word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None

    #don't need to make a classmethod since not calling any cls variables
    def match(word_list, expecting):
        if word_list:
            word = word_list.pop(0) #without 0 here you're returning last not first
            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None

    @classmethod
    def skip(cls, word_list, word_type):
        while cls.peek(word_list) == word_type:
            cls.match(word_list, word_type)

    @classmethod
    def parse_verb(cls, word_list):
        cls.skip(word_list, 'stop')
        if cls.peek(word_list) == 'verb':
            return cls.match(word_list, 'verb')
        else:
            raise ParserError('Expecting a verb next')

    @classmethod
    def parse_object(cls, word_list):
        cls.skip(word_list, 'stop')
        if cls.peek(word_list) == 'noun':
            return cls.match(word_list, 'noun')
        elif cls.peek(word_list) == 'direction':
            return cls.match(word_list, 'direction')
        else:
            raise ParserError('Expecting a noun or direction next.')

    @classmethod
    def parse_subject(cls, word_list):
        cls.skip(word_list, 'stop')
        if cls.peek(word_list) == 'noun':
            return cls.match(word_list, 'noun')
        elif cls.peek(word_list) == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError('Expecting a noun or a verb.')

    @classmethod
    def parse_sentence(cls, word_list):
        subj = cls.parse_subject(word_list)
        verb = cls.parse_verb(word_list)
        obj = cls.parse_object(word_list)

        return Sentence(subj, verb, obj)

if __name__ == "__main__":
    import lexicon
    s = 'run north'
    x = lexicon.scan(s)
    print(x)
    y = Sentence.parse_sentence(x)
    print(y.subj)
    print(y.verb)
    print(y.obj)
    print(y)
