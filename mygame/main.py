"""This is the main file for the game that I'm coding."""


from corridor import CentralCorridor
from armory import LaserWeaponArmory
from bridge import TheBridge
from escape_pod import EscapePod
from death import Death
from finished import Finished
from map import Map


# Engine is responsible for iterating through rooms and deciding outcome.
class Engine(object):

    def __init__(self, scene_map):
        print("///loading the map...")
        self.scene_map = scene_map

    def play(self):
        print("///setting the first and last scenes, only ONCE...")
        # Starts with CentralCorridor()
        current_scene = self.scene_map.opening_scene()
        # Starts and stays at Finished()
        last_scene = self.scene_map.next_scene('finished')

        def recursive_action(current_scene):
            print("///loading the next scene...")
            # This both enters the current scene and returns the next scene name
            next_scene_name = current_scene.enter()
            print("ready to move?")
            move = input("> ")
            if move == "yes":
                # This fetches the next method after #CentralCorridor() etc
                current_scene = self.scene_map.next_scene(next_scene_name)
            else:
                # This fetches Death.
                current_scene = self.scene_map.next_scene("death")
            return recursive_action(current_scene)

        recursive_action(current_scene)

        current_scene.enter()

# Play!
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
