"""This module defines the overarching scene class used in the game I coded!"""


__all__ = ["Scene"]


import sys


# The scene class is a template for other subclasses, doesn't do anything itself
class Scene(object):

    def enter(self):
        print("this scene is not yet configured")
        print("subclass it and implement enter().")
        sys.exit(1)
