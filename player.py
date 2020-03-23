from random import choice


class Blob:
    def __init__(self, x, y, blob_id, world):
        self.blob_id = blob_id
        self.x, self.y = x, y
        self.inventory = 0
        self.world = world.get_food_locations()  # Blob knows the coordinates of food

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

    def direction_choice(self):
        food_locations = self.world
        a, b = Blob.find_nearest_location(self.x, self.y, food_locations)
        direction = Blob.get_near_to(self.x, self.y, a, b)
        return direction

    @classmethod
    def step_distance(cls, x, y, a, b):
        return abs(a - x) + abs(y - b)

    @classmethod  # Warning : if there is an equality, one location among the shortest will be returned
    def find_nearest_location(cls, x, y, list_of_locations):
        minimum_distance = 1000000
        nearest_location = ()
        for (a, b) in list_of_locations:
            if Blob.step_distance(x, y, a, b) < minimum_distance:
                nearest_location = a, b
                minimum_distance = Blob.step_distance(x, y, a, b)
        return nearest_location

    @classmethod
    def get_near_to(cls, x, y, a, b):
        right_directions = []
        x_difference = a - x
        y_difference = b - y
        if x_difference > 0:
            right_directions.append('r')
        elif x_difference < 0:
            right_directions.append('l')
        if y_difference > 0:
            right_directions.append('d')
        elif y_difference < 0:
            right_directions.append('u')
        return choice(right_directions)
