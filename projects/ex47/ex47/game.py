class Room(object):
    """
    >>> center = Room('center', 'this is the center room')
    >>> west = Room('west', 'this is the west room')
    >>> center.add_paths({'west': west})
    >>> center.go('west')
    west
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

# room = Room('livingroom','desc')
# room.add_paths({'key':'value'})
# print(room.paths)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
