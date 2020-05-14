"""This module defines the Finished class used in the game I coded!"""


__all__ = ["Finished"]


import sys
from scene import Scene


class Finished(Scene):

    def enter(self):
        print('you won!!!')
        sys.exit(0)
