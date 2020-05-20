from world import World
from display import Display


class Game:
    def __init__(self, nb_rounds=10, nb_turns=10, width=10, height=10,
                 food_quantity=20, nb_blobs=4):
        self.width = width
        self.height = height
        self.food_quantity = food_quantity
        self.nb_blobs = nb_blobs
        self.nb_turns = nb_turns
        self.nb_rounds = nb_rounds
        self.world = World(self.width, self.height)
        self.game_stats = []

    def round(self):
        for turn in range(self.nb_turns):
            print('Turn : ' + str(turn))
            self.turn()

    def turn(self):
        for blob in self.world.blobs:
            if len(self.world.food) > 0:
                self.world.move_blob(blob)
        Display(self.world).display()

    def giving_phase(self):
        print("===== GIVING PHASE =====")
        for giver_index, blob in enumerate(self.world.blobs):
            if blob.inventory > 2:
                blob.give(giver_index)
        print("Generosity matrix : \n {}".format(self.world.generosity_matrix))

    def deaths_phase(self):
        print("===== DEATHS PHASE =====")
        death_list = []
        for blob_index, blob in enumerate(self.world.blobs):
            if blob.inventory < 1:
                death_list.append(blob_index)
        self.world.remove_blobs(death_list)
        if len(death_list) == 0:
            print("All blobs made it to the next round! Yay!")
        else:
            for i in death_list:
                print("Blob #{} died. RIP.".format(i))

    def reproduction_phase(self):
        print("===== REPRODUCTION PHASE =====")
        for blob_index, blob in enumerate(self.world.blobs):
            if blob.inventory > 1:
                self.world.duplicate_blob(blob)
                print("Blob #{} reproduced!".format(blob_index))

    def run(self):
        self.world.add_blobs(self.nb_blobs)
        Display(self.world).display()

        for i in range(self.nb_rounds):
            stats = {}
            self.world.add_food(self.food_quantity)
            print("////// Round number {} /////".format(i))
            self.round()
            self.giving_phase()
            self.deaths_phase()
            self.reproduction_phase()
            stats['food_left'] = len(self.world.food)
            self.world.delete_food()
            self.world.delete_remaining_blobs_food()
            stats = {'nb_blobs': self.nb_blobs,
                     'gratefulness': [blob.gratefulness for blob in self.world.blobs],
                     'altruism': [1 - self.world.generosity_matrix[i, i] for i in range(self.nb_blobs)]}
            self.game_stats.append(stats)
