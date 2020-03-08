import random
import numpy as np

class Food:
    def __init__(self, world, food_id, x, y, quantity = 1):
        self.food_id = food_id
        self.x, self.y = x, y
        self.world = world
        self.quantity = quantity

class Player:
    def __init__(self, world, player_id, x, y):
        self.player_id = player_id
        self.x, self.y = x, y
        self.world = world
        self.food_inventory = 0

    def where_is_arrival(self, direction):
        x, y = self.x, self.y

        if direction == "l":
            end_slot = x - 1, y
        elif direction == "r":
            end_slot = x + 1, y
        elif direction == "u":
            end_slot = x, y - 1
        elif direction == "d":
            end_slot = x, y + 1
        else:
            end_slot = None
        return end_slot

    def move(self, direction):
        where_to = self.where_is_arrival(direction)
        self.world.move_player(self.player_id, where_to)


class World:
    RANGE_FOOD = 1
    RANGE_PLAYER = 1000
    RANGE_END = 1999

    def __init__(self, length, height):
        # la fonction d'initialisation
        # le plateau
        self.create_empty_board(length, height)
        # les joueurs
        self.players = {} # dict (identiifant => le joueur)
        self.food = {} # dict (identiifant => food)
        # tout l'enjeu sera de maintenir le plateau en phase avec les éléments dessus

    def create_empty_board(self, length, height):
        self.length = length
        self.height = height
        self.board = np.zeros((height, length), dtype=int)  # crée une matrice de zéros

    def get_dimensions(self):
        return self.length, self.height

    def generate_coordinates(self):
        # j'aime pas trop le fait que tu utilises le noms height et length en même temps que x et y.
        # ca demande de se rappeler
        # j'ai simplifié la fonction
        return random.randrange(self.length), random.randrange(self.height)

    def is_on_the_board(self, x, y):
        return x in range(self.length) and y in range(self.height)

    def tile_is_empty(self, x, y):
        # je répond faux si hors du plateau
        if not self.is_on_the_board(x, y):
            return False
        # note comment j'ai raccourci
        return self.board[y][x] == 0

    def random_empty_tile(self):
        # j'ai simplifié
        while True:
            x, y = self.generate_coordinates()
            if self.tile_is_empty(x, y):
                break
        return x, y

    def add_food(self, food_quantity):
        for _ in range(food_quantity):
            x, y = self.random_empty_tile()
            # Trouve un numéro d'identifiant libre (1 de plus que le max)
            food_id = 0
            if len(self.food) > 0:
                food_id = max(f_id for f_id, _ in self.food.items()) + 1
            if food_id >= World.RANGE_PLAYER:
                raise('Impossible to add food')
            food = Food(self, food_id, x, y)
            self.food[food_id] = food
            self.board[y][x] = food_id + World.RANGE_FOOD

    def add_one_player(self):
        x, y = self.random_empty_tile()
        # Trouve un numéro d'identifiant libre (1 de plus que le max)
        player_id = 0
        if len(self.players) > 0:
            player_id = max(p_id for p_id, _ in self.players.items()) + 1
        if player_id >= World.RANGE_END:
            raise ('Impossible to add player')
        player = Player(self, player_id, x, y)
        self.players[player_id] = player
        self.board[y][x] = player_id + World.RANGE_PLAYER

    def add_random_players(self, nb_players):
        for _ in range(nb_players):
            self.add_one_player()

    def is_unoccupied(self, x, y):
        cell_content = self.board[y][x]
        return not (cell_content >= World.RANGE_PLAYER and cell_content < World.RANGE_END)

    def i_can_move(self, end_slot):
        x, y = end_slot
        # J'ai dû intervertir les deux test pour éviter un bug
        return self.is_on_the_board(x, y) and self.is_unoccupied(x, y)

    # attention au changement de convention. parfois tu passes un couple (x,y) en 1 paramètre, parfois deux paramètres x et y
    # c'est pas cohérent
    def there_is_food(self, end_slot):
        x, y = end_slot
        cell_content = self.board[y][x]
        return cell_content >= World.RANGE_FOOD and cell_content < World.RANGE_PLAYER

    def move_player(self, player_id, end_slot):
        if player_id not in self.players or end_slot is None or not self.i_can_move(end_slot):
            return False
        x, y = end_slot
        player = self.players[player_id]
        if self.there_is_food(end_slot):
            food_id = self.board[y][x] - World.RANGE_FOOD
            if food_id in self.food: # normalement, c'est toujours vrai
                # le joueur mange la nourriture
                player.food_inventory += self.food[food_id].quantity
                # on enleve la nourriture de la liste
                del self.food[food_id]
        # On fait le déplacement sur le plateau
        self.board[y][x] = self.board[player.y][player.x]
        self.board[player.y][player.x] = 0
        # on met à jour l'état du joueur
        player.x , player.y = x, y


class WorldPrinter:
    def __init__(self, world):
        self.world = world

    def print(self):
        print()
        for y in range(world.height):
            print("|", end='')
            for x in range(world.length):
                print("{:5d}|".format(self.world.board[y][x]), end='')
            print()


# Code principal, pour tester
def create_world(length, height, food_quantity, nb_players):
    # pourrait être mis dans la Classe World. Mais à débattre
    world = World(length, height)
    world.add_food(food_quantity)
    world.add_random_players(nb_players)
    return world

random.seed(2)
world = create_world(10, 4, 5, 4)
printer = WorldPrinter(world)
printer.print()

first_player = world.players[0]
first_player.move('u')
printer.print()
first_player.move('r')
printer.print()
first_player.move('l')
printer.print()
first_player.move('d')
printer.print()
first_player.move('d')
printer.print()
first_player.move('d')
printer.print()
first_player.move('r')
printer.print()
