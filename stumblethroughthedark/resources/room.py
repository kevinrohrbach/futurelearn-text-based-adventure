"""Create Room class."""


class Room():
    """This class represents rooms in the game."""

    def __init__(self, room_name):
        """Hold all the fields for a room."""
        self.name = room_name  # room name key
        self.narrative = None  # room description to be printed
        self.north = None  # room to the north
        self.east = None  # room to the east
        self.south = None  # room to the south
        self.west = None  # room to the west
        self.up = None  # room above
        self.down = None  # room below
        self.content = []
        # TODO: Add methods to rooms
