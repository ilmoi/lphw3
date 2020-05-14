class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    # returns the value associated with the key in the paths dictionary
    def go(self, direction):
        return self.paths.get(direction, None)

    # need to pass an iterable of len2 = tuple, dictionary, key=value
    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room('Central Corridor', 'Gothons invaded your ship. You need to blow it up while escaping in a pod. You\'re in the corridor and a GOTHON JUMPS AT YOU!')
laser_weapon_armory = Room('Laser Weapon Armory', 'You defeat the gothon. You move to the armory. You find the bomb. You need to guess the code.')
the_bridge = Room('The Bridge', 'You get the bomb. You rush to the birdge. Youre facing another 5 gothons.')
escape_pod = Room('Escape Pod', 'You beat the fuckers. You plant the bomb. Which pod do you take?')
the_end_winner = Room('The End', 'You pick the right pod and escape right before explosion. YOU WON!!!!')
the_end_loser = Room('The End', 'You pick a shitty pod tha blows up on you in precisely the wrong moment. FUCKING LOSER.')
generic_death = Room('Death', 'You died.')

START = 'central_corridor'

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

laser_weapon_armory.add_paths({
    '0123': the_bridge,
    '*': generic_death
})

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

#thus the only rooms that dont have a next room are: the_end_loser, the_end_winner, generic_death

# loads the room object using underscored description
def load_room(name):
    # he said there's a sec issue here - "who gets to set the name? ca that expose a variable?" what's a better solution than sec lookup?
    return globals().get(name)

# returns underscored description from room object. opposite of above
def name_room(room):
    # same sec problem
    for key, value in globals().items():
        if value == room:
            return key
