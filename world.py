from random import randrange, choice
from player import Blob
import numpy as np


class Food:
    def __init__(self, quantity=1):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity


class World:
    def __init__(self, width=10, height=10,
                 mutation_intensity=0.2, mutation_probability=0.5):
        self.width = width
        self.height = height
        self.mutation_intensity = mutation_intensity
        self.mutation_probability = mutation_probability
        self.food = {}
        self.blobs = np.array([])
        self.generosity_matrix = np.array([[]])

    # Intermediary mvt functions

    def get_dimensions(self):
        return self.width, self.height

    def generate_coordinates(self):
        return randrange(self.width), randrange(self.height)

    def is_on_the_board(self, x, y):
        return x in range(self.width) and y in range(self.height)

    def get_blob_positions(self):
        return [(blob.x, blob.y) for blob in self.blobs]

    def there_is_no_player(self, x, y):
        return (x, y) not in self.get_blob_positions()

    def tile_is_empty(self, x, y):
        return (x, y) not in self.food and (x, y) not in self.get_blob_positions()

    def i_can_move(self, x, y):
        return self.there_is_no_player(x, y) and self.is_on_the_board(x, y)

    def there_is_food(self, x, y):
        return (x, y) in self.food

    def get_food_locations(self):
        return self.food.keys()

    # World generation

    def random_empty_tile(self):
        while True:
            x, y = self.generate_coordinates()
            if self.tile_is_empty(x, y):
                break
        return x, y


    def add_food(self, food_quantity):
        for _ in range(food_quantity):
            x, y = self.random_empty_tile()
            self.food[x, y] = Food()

    def delete_food(self):
        self.food = {}

    def stochastify_matrix(self):
        sum_vector = np.sum(self.generosity_matrix, axis=1)
        self.generosity_matrix = self.generosity_matrix / sum_vector[:, None]

    def add_blobs(self, nb_new_blobs):
        for _ in range(nb_new_blobs):
            x, y = self.random_empty_tile()
            self.blobs = np.append(self.blobs, Blob(x, y, self))

            # Update generosity_matrix
            nb_existing_blobs = self.blobs.size
            # If this is the first blob added, the generosity_matrix is just
            # a [[1]]. Doing this prevents a bug.
            if nb_existing_blobs == 1:
                self.generosity_matrix = np.array([[1]])
                continue
            column = np.zeros((nb_existing_blobs - 1, 1))
            self.generosity_matrix = np.append(self.generosity_matrix,
                                               column, axis=1)
            line = abs(np.random.randn(1, nb_existing_blobs))
            line = line / np.sum(line)
            self.generosity_matrix = np.append(self.generosity_matrix,
                                               line, axis=0)
        print("generosity_matrix : \n {} \n -----------".format(
            self.generosity_matrix))

    @staticmethod
    def mutation(p):
        return np.random.choice([True, False], p=[p, 1 - p])

    def duplicate_blob(self, parent):
        # Testé

        # New Blob
        x, y = self.random_empty_tile()
        new_gratefulness = parent.gratefulness
        new_vexation = parent.vexation
        if World.mutation(self.mutation_probability):
            new_gratefulness *= (1
                                 + np.random.choice([-1, 1])
                                 * self.mutation_intensity)
        if World.mutation(self.mutation_probability):
            new_vexation *= (1
                             + np.random.choice([-1, 1])
                             * self.mutation_intensity)
        new_blob = Blob(x, y, self, gratefulness=new_gratefulness,
                        vexation=new_vexation)
        self.blobs = np.append(self.blobs, new_blob)

        # Update generosity_matrix
        nb_existing_blobs = self.blobs.size
        column = np.zeros((nb_existing_blobs - 1, 1))
        self.generosity_matrix = np.append(self.generosity_matrix,
                                           column, axis=1)
        line = abs(np.random.randn(1, nb_existing_blobs))
        line = line / np.sum(line)
        self.generosity_matrix = np.append(self.generosity_matrix,
                                           line, axis=0)

    def remove_blobs(self, death_list):
        # On supprime un blob
        self.blobs = np.delete(self.blobs, death_list)

        # On met à jour la matrice de connectivité
        self.generosity_matrix = np.delete(self.generosity_matrix,
                                           death_list, axis=0)
        self.generosity_matrix = np.delete(self.generosity_matrix,
                                           death_list, axis=1)
        self.stochastify_matrix()

    def delete_remaining_blobs_food(self):
        # On supprime la nourriture qu'il reste aux survivants à la fin du tour
        for blob in self.blobs:
            blob.inventory = 0

    # Movement mechanic
    def move_blob(self, blob):
        direction = blob.direction_choice()
        x, y = blob.where_is_arrival(direction)
        if self.i_can_move(x, y):
            blob.move(x, y)
        if self.there_is_food(x, y):
            blob.eats(self.food[x, y])
            del self.food[x, y]
