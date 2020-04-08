from random import randrange, choice
from player import Blob


class Food:
    def __init__(self, quantity=1):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity


class World:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.food = {}
        self.blobs = {}

    # Intermediary mvt functions

    def get_dimensions(self):
        return self.width, self.height

    def generate_coordinates(self):
        return randrange(self.width), randrange(self.height)

    def is_on_the_board(self, x, y):
        return x in range(self.width) and y in range(self.height)

    def there_is_no_player(self, x, y):
        return (x, y) not in self.get_blob_positions()

    def tile_is_empty(self, x, y):
        return (x, y) not in self.food and (x, y) not in self.get_blob_positions()

    def i_can_move(self, x, y):
        return self.there_is_no_player(x, y) and self.is_on_the_board(x, y)

    def there_is_food(self, x, y):
        return (x, y) in self.food

    def get_blob_positions(self):
        return [(blob.x, blob.y) for blob in self.blobs.values()]

    def get_food_locations(self):
        return self.food.keys()

    # World generation

    def random_empty_tile(self):
        while True:
            x, y = self.generate_coordinates()
            if self.tile_is_empty(x, y):
                break
        return x, y

    def random_border_tile(self):
        w, h = self.width, self.height
        while True:
            borders = [(0, randrange(h)), (w - 1, randrange(h)),
                       (randrange(w), 0), (randrange(w), h - 1)]
            x, y = choice(borders)
            if self.tile_is_empty(x, y):
                return x, y

    def add_food(self, food_quantity):
        for _ in range(food_quantity):
            x, y = self.random_empty_tile()
            self.food[x, y] = Food()

    def add_blobs(self, nb_blobs):
        for blob_id in range(nb_blobs):
            x, y = self.random_border_tile()
            self.blobs[blob_id] = Blob(x, y, blob_id, self)

    def create_world(self, food_quantity=5, nb_blobs=4):
        self.add_food(food_quantity)
        self.add_blobs(nb_blobs)

    # Movement mechanic

    def move_blob(self, blob_id, direction):
        if blob_id not in self.blobs:
            raise Exception('Incorrect blob_icon id !')
        current_blob = self.blobs[blob_id]  # I get the corresponding blob_icon
        x, y = current_blob.where_is_arrival(direction)
        if self.i_can_move(x, y):
            current_blob.move(x, y)
        if self.there_is_food(x, y):
            current_blob.eats(self.food[x, y])
            del self.food[x, y]
