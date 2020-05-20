from random import choice

# dummy commit

class Blob:

    def __init__(self, x, y, world,
                 gratefulness=0.5, vexation=0.5):
        self.x, self.y = x, y
        self.inventory = 0
        self.world = world
        self.generosity_vector = []
        self.gratefulness = gratefulness
        self.vexation = vexation

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
        dx, dy = {"l": (-1, 0), "r": (1, 0), "u": (0, -1),
                  "d": (0, 1)}[direction]
        return x + dx, y + dy

    def move(self, x, y):
        self.x, self.y = x, y

    def eats(self, food):
        self.inventory += food.get_quantity()

    def direction_choice(self):

        food_locations = self.world.get_food_locations()
        a, b = Blob.find_nearest_location(self.x, self.y, food_locations)
        direction = Blob.get_near_to(self.x, self.y, a, b)
        return direction

    def get_generosity_vector(self, giver_index):
        return self.world.generosity_matrix[giver_index]

    def choose_receivers(self, giver_index, nb_receivers):
        self.generosity_vector = self.get_generosity_vector(giver_index)
        receivers_indexes = np.random.choice(
                            len(self.world.blobs),
                            nb_receivers,
                            p=self.generosity_vector)
        return receivers_indexes

    def become_grateful(self, giver_index, receiver_index):
        old_coeff = self.world.generosity_matrix[receiver_index, giver_index]
        if old_coeff == 0:
            new_coeff = 0.05 # (low arbitrary value)
        else:
            new_coeff = old_coeff * (1 + self.gratefulness)
        if new_coeff >= 1:
            self.world.generosity_matrix[receiver_index, :] *= 0
            self.world.generosity_matrix[receiver_index, giver_index] = 1
        else:
            update_factor = (1 - new_coeff) / (1 - old_coeff)
            self.world.generosity_matrix[receiver_index, :] *= update_factor
            self.world.generosity_matrix[receiver_index, giver_index]=new_coeff


    def give(self, giver_index):
        nb_extra_food = self.inventory - 2
        receivers_indexes = self.choose_receivers(giver_index=giver_index,
                                                    nb_receivers=nb_extra_food)
        self.inventory -= nb_extra_food
        for receiver_index in receivers_indexes:
            print("Blob #{} gives 1 food to blob #{}".format(giver_index,
                receiver_index))
            self.world.blobs[receiver_index].inventory += 1
            self.become_grateful(giver_index, receiver_index)

    @staticmethod
    def step_distance(x, y, a, b):
        return abs(a - x) + abs(y - b)

    @staticmethod  # Warning : if there is an equality, one location among the shortest will be returned
    def find_nearest_location(x, y, list_of_locations):
        minimum_distance = 1000000
        nearest_location = ()
        for (a, b) in list_of_locations:
            if Blob.step_distance(x, y, a, b) < minimum_distance:
                nearest_location = a, b
                minimum_distance = Blob.step_distance(x, y, a, b)
        return nearest_location

    @staticmethod
    def get_near_to(x, y, a, b):
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
