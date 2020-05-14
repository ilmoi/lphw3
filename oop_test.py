import random
from urllib.request import urlopen
import sys

WORD_URL = 'http://learncodethehardway.org/words.txt'
WORDS = []


PHRASES = {
    "class %%%(%%%):" : "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" : "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)" : "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()" : "set *** to an instance of class %%%.",
    "***.***(@@@)" : "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'" : "From *** get the *** attribute and set it to '***'."
}
# %%% = class names, *** = class attributes or methods, @@@ params for those class methods.
# But then *** also objects...

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    # print(type(word.decode("utf-8")))
    WORDS.append(str(word.strip(), encoding="utf-8"))
#ok so this shit just puts all the words into a list without padding spaces

# print(WORDS)

def convert(snippet, phrase):
    # print(snippet, phrase)
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    # count how many %%% are in this fucking snippet, whatever it is
    # then sample that many words from WORDS, and capitalize them
    # then assign all those words to class_names

    # print(class_names)

    other_names = random.sample(WORDS, snippet.count("***"))
    # count how many *** are in the snippet
    # then sample that many words from WORDS
    # assign them to other_names

    # print(other_names)

    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    # count the number of @@@ in the snippet
    # for each of those @@@
    # pick a random number between 1 and 3 for param_count
    # join that many words from WORDS into a single parameter string
    # append that word to param_names

    #thus so far we've created some class names, some other names and some param names

    # print(param_names)

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class class_names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other other_names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results
    #we're returning snippet but with new randon names in there

#keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        #ok so the fucking snippets thing is nothing more than a list of keys from above dict

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
