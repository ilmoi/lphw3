from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room(
        'GoldRoom',
        """This room is full of gold"""
    )
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room('Center','center room')
    north = Room('North', 'north room')
    south = Room('South', 'south room')

    center.add_paths({'north': north,'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room('Start', 'start room')
    west = Room('Trees', 'there are trees here')
    down = Room('Dungeon', 'its dark here')

    start.add_paths({'west': west,'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")
