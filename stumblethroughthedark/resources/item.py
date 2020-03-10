"""Define the Item class."""


class Item():
    """This class represents items in the game."""

    def __init__(self):
        """Hold all fields for Item."""
        self.name = ""  # name of the object
        self.description = ""  # description of item to be printed

    def set_description(self, item_description):
        """Set item descriptoin."""
        self.description = item_description

    def get_description(self):
        """Get item description."""
        return self.description

    def get_name(self):
        """Get item name."""
        return self.name

    def describe(self):
        """Describe item."""
        print(self.description)

# TODO: Add additional attributes and methods for items
