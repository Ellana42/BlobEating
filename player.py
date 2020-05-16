from numpy.random import choice
# dummy commit

class Blob:
    def __init__(self, x, y, world, blob_id = 0,
                gratefulness = 0.5, vexation = 0.5):
        self.blob_id = blob_id                  # il y a des modules pour mettre des identifiants uniques si on en a besoin
        self.x, self.y = x, y
        self.inventory = 0
        self.world = world
        self.perceived_world = world.get_food_locations()  # Blob knows the coordinates of food
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

    def move(self, new_x, new_y):
        self.x, self.y = new_x, new_y  # added `new_` where relevant for clarity [Rémi]

    def eats(self, food):
        self.inventory += food.get_quantity()

    def direction_choice(self):
        food_locations = self.perceived_world
        a, b = Blob.find_nearest_location(self.x, self.y, food_locations)
        direction = Blob.get_near_to(self.x, self.y, a, b)
        return direction

    def get_generosity_vector(self, giver_index):
        return self.world.generosity_matrix[giver_index]


    def choose_receivers(self, giver_index, nb_receivers):
        self.generosity_vector = self.get_generosity_vector(giver_index)
        receivers = choice(self.world.blobs, nb_receivers, p=self.generosity_vector)
        return receivers

    def become_grateful(self, giver_index, reciever_index):
        # à tester
        old_coeff = world.generosity_matrix[reciever_index, giver_index]
        row_sum = old_coeff * self.gratefulness + 1
        world.generosity_matrix[reciever_index, :] /= row_sum
        world.generosity_matrix[reciever_index, giver_index] = (old_coeff
                                                            * self.gratefulness)

    def give(self, giver_index):
        nb_extra_food = self.inventory - 2
        receivers = self.choose_receivers(giver_index = giver_index, nb_receivers = nb_extra_food)
        self.inventory += -nb_extra_food
        for receiver_index, reciever in enumerate(receivers) :
            receiver.inventory += 1
            become_grateful(giver_index, reciever_index)


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
