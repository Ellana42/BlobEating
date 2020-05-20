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

    def round(self):
        for turn in range(self.nb_turns):
            print('Turn : ' + str(turn))
            self.turn()

    def turn(self):
        for blob in self.world.blobs:
            self.world.move_blob(blob)
        Display(self.world).display()

    def giving_phase(self):
        for giver_index, blob in enumerate(self.world.blobs):
            if blob.inventory > 2:
                blob.give(giver_index)

    def deaths_phase(self):
        for blob_index, blob in enumerate(self.world.blobs):
            if blob.inventory < 1:
                world.remove_blob(blob_index)

    def reproduction_phase(self):
        for blob_index, blob in enumerate(self.world.blobs):
            if blob.inventory > 1:
                self.world.duplicate_blob(blob, blob_index)

    def score_board(self):
        winners = []
        current_best_score = 0
        for blob in self.world.blobs.values():
            print('Blob number {} got {} foods'.format(
                blob.get_blob_id(), blob.get_inventory()))
            if blob.get_inventory() > current_best_score:
                winners = [blob.get_blob_id()]
                current_best_score = blob.get_inventory()
            elif blob.get_inventory() == current_best_score:
                winners.append(blob.get_blob_id())
        print('The Blobs with the most food are : ' + str(winners))

    def game_run(self):
        self.world.add_blobs(self.nb_blobs)
        Display(self.world).display()

        for i in range(self.nb_rounds):
            self.world.add_food(self.food_quantity)
            print("////// Round number {} /////".format(i))
            self.round()
            self.giving_phase()
            self.deaths_phase()
            self.reproduction_phase()
            world.delete_food()
            world.delete_remaining_blobs_food()
            world.update_blobs()  # update each blobs generosity vector

        self.score_board()
