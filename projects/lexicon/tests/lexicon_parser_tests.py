from nose.tools import *
from lexicon import lexicon_parser

def test_parser_error():
    pass

def test_sentence():
    s = lexicon_parser.Sentence(('a','a'),('b','b'),('c','c'))
    assert_equal(s.subj,'a')
    assert_equal(s.verb,'b')
    assert_equal(s.obj,'c')

def test_peek():
    w = [('first','first_word'),('second','second_word')]
    assert_equal(lexicon_parser.peek(w),'first')
    w = []
    assert_equal(lexicon_parser.peek(w), None)

def test_match():
    w = [('first','first_word'),('second','second_word')]
    assert_equal(lexicon_parser.match(w, 'first'),('first','first_word'))
    assert_equal(lexicon_parser.match(w, 'first'),None)
    w = []
    assert_equal(lexicon_parser.match(w, 'first'), None)

def test_skip():
    w = [('first','first_word'),('second','second_word')]
    lexicon_parser.skip(w,'first')
    assert_equal(w, [('second','second_word')])

def test_parse_verb():
    w = [('verb','first_verb'),('second','second_word')]
    assert_equal(lexicon_parser.parse_verb(w), ('verb','first_verb'))
    assert_raises(lexicon_parser.ParserError, lexicon_parser.parse_verb, w) #ok so exception type w/o brackets > function w/o brackets > arguments for function

def test_parse_object():
    pass

def test_parse_subject():
    pass

def test_parse_sentence():
    pass
