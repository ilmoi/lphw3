"""This module defines the Armory class used in the game I coded!"""


__all__ = ["LaserWeaponArmory"]


from scene import Scene


class LaserWeaponArmory(Scene):

    def enter(self):
        print("you arrive in the armory, guess the pin, and obtain the weapon! ONWARDS!")
        return 'the_bridge'
