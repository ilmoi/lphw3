"""this will be fun!"""

def scan(sentence):
    words = sentence.split()
    ret = []
    for word in words:
        if word in ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']:
            tup = ('direction', word)
        elif word in ['go', 'stop', 'kill', 'eat', 'run']:
            tup = ('verb', word)
        elif word in ['the', 'in', 'of', 'from', 'at', 'it']:
            tup = ('stop', word)
        elif word in ['door', 'bear', 'princess', 'cabinet']:
            tup = ('noun', word)
        else:
            try:
                num = int(word)
            except ValueError:
                tup = ('error', word)
            else:
                tup = ('number', word)

        ret.append(tup)

    return ret
