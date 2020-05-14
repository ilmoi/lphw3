"""This module defines the Bridge class used in the game I coded!"""


__all__ = ["TheBridge"]


from scene import Scene


class TheBridge(Scene):

    def enter(self):
        print("you arrive at the bridge, see another monster, and defeat the fucker! ONWARDS!")
        return "escape_pod"
