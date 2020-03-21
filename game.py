from world import World
from display import Display


class Game:
    def __init__(self, width=10, height=10, food_quantity=4, nb_blobs=4, turns=10):
        self.width = width
        self.height = height
        self.food_quantity = food_quantity
        self.nb_blobs = nb_blobs
        self.turns = turns

    '''def game_run(self):
        world = World(self.width, self.height)
        world.create_world(self.food_quantity, self.nb_blobs)
        Display(world).display()
        for _ in range(self.turns):'''
