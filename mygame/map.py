"""This is the map class for the game I coded."""


__all__ = ["Map"]


from corridor import CentralCorridor
from armory import LaserWeaponArmory
from bridge import TheBridge
from escape_pod import EscapePod
from death import Death
from finished import Finished


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        print("you arrive at the abandoned ship. lets figure shit out")
        return self.next_scene(self.start_scene)
