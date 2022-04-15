class Room:
    directions = {
        "south": 0,
        "west": 1,
        "north": 2,
        "east": 3
    }

    def __init__(self, name):
        self.name = name
        self.description = ""
        self.character = None
        self.item = None
        self.linked_rooms = dict()

    def get_details(self):
        print(self.description)

    def set_description(self, description):
        self.description = description

    def link_room(self, room, direction):
        self.linked_rooms[self.directions[direction]] = room
        room.linked_rooms[(self.directions[direction] + 2) % 4] = self

    def move(self, direction):
        if self.directions[direction] in self.linked_rooms:
            return self.linked_rooms[self.directions[direction]]
        else:
            return self

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item


class Enemy:
    defeated = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.weakness = None
        self.conversation = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def set_conversation(self, conversation):
        self.conversation = conversation

    def describe(self):
        print(self.description)

    def talk(self):
        print(self.conversation)

    def fight(self, weapon):
        if weapon == self.weakness:
            Enemy.defeated += 1
            return True
        return False

    def get_defeated(self):
        return Enemy.defeated


class Item:
    def __init__(self, name):
        self.name = name
        self.description = ""

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name

