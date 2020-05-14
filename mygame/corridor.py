"""This module defines the corridor class used in the game I coded!"""


__all__ = ["CentralCorridor"]


from scene import Scene


class CentralCorridor(Scene):

    def enter(self):
        print("you arrive in the corridor, see a monster, and defeat the fucker! ONWARDS!")
        return 'laser_weapon_armory'
