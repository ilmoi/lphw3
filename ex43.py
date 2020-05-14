import sys

#L1
# overall class that defines what all scenes should be able to do
class Scene(object):

    #interesting, no init method from which I gather we never instantiate this?

    def enter(self):
        pass



# engine class that pushes the game forward
class Engine(object):

    def __init__(self, scene_map):
        print("///loading the map...")
        self.scene_map = scene_map

    def play(self):
        if not self.scene_map.scene_name:
            print("///time to play - loading opening scene...")
            self.scene_map.opening_scene()

        print("ready to move?")
        move = input("> ")
        if move == "yes":
            print("///loading next scene...")
            self.scene_map.next_scene(self.scene_map.scene_name)
        else:
            print("///loading next scene...")
            self.scene_map.next_scene("death")

    def win(self):
        print("congrats you won mate")
        sys.exit(0)

    def lose(self):
        print("you lost mate")
        sys.exit(0)



#map class takes care of all the navigation
class Map(object):

    def __init__(self, start_scene):
        self.start_scene = start_scene
        self.scene_name = None

    # this should map out all the relations
    def next_scene(self, scene_name):
        self.scene_name = scene_name

        if self.scene_name == "central_corridor":
            central_corridor = CentralCorridor()
            central_corridor.enter()
            self.scene_name = "laser_weapon_armory"
            a_game.play()

        if self.scene_name == "laser_weapon_armory":
            laser_weapon_armory = LaserWeaponArmory()
            laser_weapon_armory.enter()
            self.scene_name = "the_bridge"
            a_game.play()

        if self.scene_name == "the_bridge":
            the_bridge = TheBridge()
            the_bridge.enter()
            self.scene_name = "escape_pod"
            a_game.play()

        if self.scene_name == "escape_pod":
            escape_pod = EscapePod()
            escape_pod.enter()
            a_game.win()

        if self.scene_name == "death":
            death = Death()
            death.enter()
            a_game.lose()

    # this should do a broad intro to the game
    def opening_scene(self):
        print("you arrive at the abandoned ship. lets figure shit out")
        self.scene_name = self.start_scene



#L2
# all the different scenes - these should only contain actions within a scene
class Death(Scene):

    def enter(self):
        print('what a fucking loser - you died!!!!')

class CentralCorridor(Scene):

    def enter(self):
        print("you arrive in the corridor, see a monster, and defeat the fucker! ONWARDS!")

class LaserWeaponArmory(Scene):

    def enter(self):
        print("you arrive in the armory, guess the pin, and obtain the weapon! ONWARDS!")

class TheBridge(Scene):

    def enter(self):
        print("you arrive at the bridge, see another monster, and defeat the fucker! ONWARDS!")

class EscapePod(Scene):

    def enter(self):
        print("finally you arrive in the escape pod area, guess the pod, plant the bomb, and eject yourself before the explosion! WINNER!")

#play
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
