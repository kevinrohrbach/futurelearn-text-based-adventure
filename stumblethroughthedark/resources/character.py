"""Define the Character class."""


class Character():
    """This class represents the characters in the game."""

    def __init__(self, char_name, char_description):
        """Hold all the character attributes."""
        self.name = char_name  # character name
        self.description = char_description
        self.conversation = None
        self.madness = None  # charter madness (maybe use 1-10)
        # TODO: Add more character traits

    def describe(self):
        """Describe this character."""
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """Set what this character will say when talked to."""
        self.conversation = conversation

    def talk(self):
        """Talk to this character."""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        """Fight with this character."""
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):
    """This class represents enemies in the game."""

    def __init__(self, char_name, char_description):
        """Hold enemy attributes."""
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        """Set weakness for this character."""
        self.weakness = weakness

    def get_weakness(self):
        """Get enemy weakness."""
        return self.weakness

    def fight(self, combat_item):
        """Fight with this enemy."""
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
