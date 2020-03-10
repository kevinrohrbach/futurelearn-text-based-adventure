"""Create Room class."""


class Room():
    """This class represents rooms in the game."""

    def __init__(self, room_name):
        """Hold all the fields for a room."""
        self.name = room_name  # room name key
        self.description = None  # room description to be printed
        self.linked_rooms = {}
        self.content = []

    def set_description(self, room_description):
        """Set room description."""
        self.description = room_description

    def get_description(self):
        """Get room description."""
        return self.description

    def get_name(self):
        """Get room name."""
        return self.name

    def describe(self):
        """Describe room."""
        print(self.description)

    def link_room(self, room_to_link, direction):
        """Links room to neighbour in specific direction."""
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        """Get full details of room."""
        print(self.name)
        print("----------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        """Move between rooms."""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
