"""This module defines the EscapePod class used in the game I coded!"""


__all__ = ["EscapePod"]


from scene import Scene


class EscapePod(Scene):

    def enter(self):
        print("finally you arrive in the escape pod area, guess the pod, plant the bomb, and eject yourself before the explosion!")
        return 'finished'
