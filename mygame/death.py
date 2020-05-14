"""This module defines the Death class used in the game I coded!"""


__all__ = ["Death"]


import sys
from scene import Scene


class Death(Scene):

    def enter(self):
        print('what a fucking loser - you died!!!!')
        sys.exit(0)
