from world import World
from display import Display


class Game:
    def __init__(self, width=10, height=10, food_quantity=20, nb_blobs=4, turns=10):
        self.width = width
        self.height = height
        self.food_quantity = food_quantity
        self.nb_blobs = nb_blobs
        self.nb_turns = nb_turns
        self.nb_rounds = nb_rounds
        self.world = World(self.width, self.height)


    def round(self) :
        for turn in range(self.turns):
            self.turn()

    def turn(self) :
        for blob in self.world.blobs:
            self.world.move_blob(
                blob_id=blob, direction=self.world.blobs[blob].direction_choice()
            )
        print('Turn : ' + str(turn))
        Display(self.world).display()


    def giving_phase(self) :
        for blob in self.world.blobs:
            if blob.inventory > 2 :
                blob.give()

    def deaths_phase(self) :
        for blob in self.world.blobs:
            if blob.inventory < 1:
                blob.die()


    def reproduction_phase(self):
        for blob in self.world.blobs:
            if blob.inventory > 1 :
                blob.reproduce()

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
        self.world.create_world(self.food_quantity, self.nb_blobs)
        Display(self.world).display()

        for i in range(round_number) :
            self.round()
            self.giving_phase()
            self.deaths_phase()
            self.reproduction_phase()
            world.delete_food()
            world.delete_remaining_blobs_food()

        self.score_board()
