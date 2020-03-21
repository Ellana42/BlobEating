from random import choice


class Blob:
    def __init__(self, x, y, blob_id):
        self.blob_id = blob_id
        self.x, self.y = x, y
        self.inventory = 0
        self.perception = None  # TODO add what the blob perceives

    def get_position(self):
        return self.x, self.y

    def get_blob_id(self):
        return self.blob_id

    def get_inventory(self):
        return self.inventory

    def where_is_arrival(self, direction):
        if direction not in "lrud":
            return None
        x, y = self.x, self.y
        dx, dy = {"l": (-1, 0), "r": (1, 0), "u": (0, -1), "d": (0, 1)}[direction]
        return x + dx, y + dy

    def move(self, x, y):
        self.x, self.y = x, y

    def eats(self, food):
        self.inventory += food.get_quantity()

    def direction_choice(self):  # TODO use perception for decision rule
        direction = choice(['l', 'r', 'u', 'd'])
        return direction
