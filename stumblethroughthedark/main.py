"""A game of cunning and other derring do."""

# from sys import exit

# import local packages
from resources.room import Room
from resources.item import Item
from resources.character import Character
from resources.character import Enemy

bedroom = Room("Bedroom")
bedroom.set_description("""
You are sitting on the edge of a bed in a dimly lit room.
There is a door to the North and a door to the East.
Beside the bed an old battery powered torch is mounted on the wall.
""")

madroom = Room("Madman's Den")
madroom.set_description("""
You are in a small room.
A madman is ranting and raving in the corner.
There is a second door on the East side of the room.
""")

waterroom = Room("Rushing Water Room")
waterroom.set_description("""
You are standing at the door of a dark room.
You can hear the sound of rushing water ahead.
""")

bedroom.link_room(madroom, 'north')
bedroom.link_room(waterroom, 'east')
madroom.link_room(bedroom, 'south')
waterroom.link_room(bedroom, 'west')

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")

madroom.set_character(dave)

current_room = bedroom

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    current_room = current_room.move(command)

# TODO: Add list of items
# TODO: Add list of characters
# TODO: Main function
