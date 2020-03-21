from world import World
from display import Display


class Game:
    def __init__(self, width=10, height=10, food_quantity=4, nb_blobs=4, turns=10):
        self.width = width
        self.height = height
        self.food_quantity = food_quantity
        self.nb_blobs = nb_blobs
        self.turns = turns

    def game_run(self):
        world = World(self.width, self.height)
        world.create_world(self.food_quantity, self.nb_blobs)
        Display(world).display()
        for turn in range(self.turns):
            for blob in world.blobs:
                world.move_blob(blob_id=blob, direction=world.blobs[blob].direction_choice())
            print('Turn : ' + str(turn))
            Display(world).display()
