from nose.tools import *
from lexicon import lexicon

def test_directions():
    assert_equal(lexicon.scan('north'), [('direction', 'north')])
    result = lexicon.scan('north south east')
    assert_equal(result, [('direction', 'north'), ('direction', 'south'), ('direction', 'east')])

def test_numbers():
    assert_equal(lexicon.scan('1234'), [('number', '1234')])

def test_error():
    assert_equal(lexicon.scan('ADSFASFDS'), [('error', 'ADSFASFDS')])

def test_all():
    result = lexicon.scan('1234 IAS south')
    assert_equal(result, [('number', '1234'),('error', 'IAS'),('direction', 'south')])
