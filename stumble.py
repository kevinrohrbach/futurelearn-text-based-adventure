"""A game of cunning and other derring do."""

# from sys import exit

# Setting up the canvas. Creating classes for rooms, items, inventory...


class Room():
    """This class represents rooms in the game."""

    def __init__(self):
        """Hold all the fields for a room."""
        self.name = ""  # room name key
        self.narrative = ""  # room description to be printed
        self.north = ""  # room to the north
        self.east = ""  # room to the east
        self.south = ""  # room to the south
        self.west = ""  # room to the west
        self.up = ""  # room above
        self.down = ""  # room below
        self.content = []
        # TODO: Add methods to rooms


class Inventory():
    """This class represents the inventory in the game."""

    def __init__(self):
        """Hold all the fields for the inventory."""
        self.capacity = 0  # definie maximum capacity of inventory
        self.content = {}  # dictionary to hold items and counts
        # TODO: Finish inventory class


class Item():
    """This class represents items in the game."""

    def __init__(self):
        """Hold all fields for Item."""
        self.name = ""  # name of the object
        self.description = ""  # description of item to be printed
        # TODO: Add methods to items


class Character():
    """This class represents the characters in the game."""

    def __init__(self):
        """Hold all the character attributes."""
        self.name = ""  # character name
        self.madness = False  # charter madness (maybe use 1-10)
        # TODO: Add more character traits

# List of rooms


room_list = []

room_1 = Room()
room_1.name = "Bedroom"
room_1.narrative = """
You are sitting on the edge of a bed in a dimly lit room.
There is a door to the North and a door to the East.
Beside the bed an old battery powered torch is mounted on the wall."""
room_1.content = ["torch"]
room_list.append(room_1)

room_2 = Room()
room_2.name = "Madman's Den"
room_2.narrative = """
You are in a small room.
A madman is ranting and raving in the corner.
There is a second door on the East side of the room.
"""
room_list.append(room_2)

room_3 = Room()
room_3.name = "Dwarf's Cavern"
room_list.append(room_3)

room_4 = Room()
room_4.name = "On the Jetty"
room_list.append(room_4)

room_5 = Room()
room_5.name = "Under the Jetty"
room_list.append(room_5)

room_6 = Room()
room_6.name = "Rushing Water Room"
room_list.append(room_6)

room_7 = Room()
room_7.name = "Gallery"
room_list.append(room_7)

room_8 = Room()
room_8.name = "Well Room"
room_list.append(room_8)

room_9 = Room()
room_9.name = "Larder"
room_list.append(room_9)

room_10 = Room()
room_10.name = "North of the Snake Pit"
room_list.append(room_10)

room_11 = Room()
room_11.name = "South of the Snake Pit"
room_list.append(room_11)

room_12 = Room()
room_12.name = "Room with a Crumbling Wall"
room_list.append(room_12)

room_13 = Room()
room_13.name = "Boudoir"
room_list.append(room_13)

room_14 = Room()
room_14.name = "East of the Troll Bridge"
room_list.append(room_14)

room_15 = Room()
room_15.name = "West of the Troll Bridge"
room_list.append(room_15)

room_16 = Room()
room_16.name = "In the River"
room_list.append(room_16)

room_17 = Room()
room_17.name = "In the River"
room_list.append(room_17)

room_18 = Room()
room_18.name = "Inn"
room_list.append(room_18)

room_19 = Room()
room_19.name = "Bottom of Staircase"
room_list.append(room_19)

room_20 = Room()
room_20.name = "Middle of Staircase"
room_list.append(room_20)

room_21 = Room()
room_21.name = "Freedom"
room_21.narrative = """
You take a few last tired steps towards the light.
At the end you need to crawl on your hands and knees through a small hole.
Finally you see the sun again for the first time in what seems days.
You swear to never go anywhere dark ever again.
"""
room_list.append(room_21)
# TODO: Finish room List

for i in room_list:
    print(i.name)


# TODO: Add list of items
# TODO: Add list of characters
# TODO: Main function
