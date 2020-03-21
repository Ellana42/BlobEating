import numpy as np
import random

random.seed(2)

possible_directions = ('l', 'r', 'u', 'd')


# Creation and setup of the board =====================================================


# Creation and setup of the board =====================================================


def create_empty_board(length, height):
    board = np.zeros((height, length), dtype=int)  # crée une matrice de zéros
    return board


# example
print(create_empty_board(10, 10))
print(create_empty_board(10, 3))
print(create_empty_board(3, 10))


def get_dimensions(board):
    length, height = len(board[0]), len(board)
    return length, height


# example
print(get_dimensions(create_empty_board(3, 10)))


def generate_coordinates(dimensions):
    length, height = dimensions
    x, y = random.randrange(length), random.randrange(height)
    return x, y


# example
for j in range(10):
    print(generate_coordinates((3, 10)))


def tile_is_empty(x, y, board):
    if board[y][x] == 0:
        return True
    else:
        return False


def random_empty_tile(board):
    dimensions = get_dimensions(board)
    while True:
        x, y = generate_coordinates(dimensions)
        if board[y][x] == 0:
            break
    return x, y


# example
print(get_dimensions(create_empty_board(2, 10)))


def add_food(food_quantity, board):
    food_location = ()
    for i in range(food_quantity):
        x, y = random_empty_tile(board)
        board[y][x] = 1
        food_location = food_location
    return board


# example
my_board = create_empty_board(3, 10)
print(add_food(5, my_board))


def create_board(height, length, food_quantity):
    return add_food(food_quantity, create_empty_board(length, height))


# Now let's add players, with an id, an inventory and a position on the board =================

# We start by creating a table which has 1 column for each information ------------------------

def create_player_table(nb_players):
    player_table = np.zeros((nb_players, 4), dtype=int)
    for player_id in range(nb_players):
        player_table[player_id][0] = player_id
    return player_table


# example
print(create_player_table(6))


# Then we give the players a position on the board ------------------------------


def assign_positions(player_table, board):
    nb_of_players = len(player_table)
    for player_id in range(nb_of_players):
        x, y = random_empty_tile(board)
        board[y][x] = 2
        player_table[player_id][2] = x  # x coordinate in 3rd slot of player description
        player_table[player_id][3] = y  # y coordinate in 4rt slot of player description
    return player_table, board


# Then we can generate our entire world !

def create_world(height, length, food_quantity, nb_players):
    board = create_board(height, length, food_quantity)
    player_table = create_player_table(nb_players)
    assign_positions(player_table, board)
    return player_table, board


# example
my_world = create_world(5, 10, 5, 4)
print(my_world[0])
print(my_world[1])


def player_eats(player_table, player_id):
    inventory_column = 1
    player_table[player_id][inventory_column] += 1
    return player_table


# example
print(player_eats(create_player_table(6), 2))


# possible_directions will be coded by l for left, r right, u up and d down


# we first need to check whether how is the spot we are trying to move to -----------------------


def is_on_the_board(x, y, board):
    length, height = get_dimensions(board)
    if x in range(length) and y in range(height):
        return True
    else:
        return False


# example
my_board = create_empty_board(3, 3)
print(is_on_the_board(1, 2, my_board))
print(is_on_the_board(0, 3, my_board))
print(is_on_the_board(6, 2, my_board))


# this is different from tile_is_empty because we just check for other players

def is_unoccupied(x, y, board):
    if board[y][x] == 2:
        return False
    else:
        return True


def i_can_move(end_slot, board):
    x, y = end_slot
    return is_unoccupied(x, y, board) and is_on_the_board(x, y, board)


def there_is_food(end_slot, board):
    x, y = end_slot
    if board[y][x] == 1:
        return True
    else:
        return False


# Then we need to know were our mvt gets us


def where_is_arrival(direction, actual_position):
    x, y = actual_position

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


# example
print(where_is_arrival("l", (3, 3)))
print(where_is_arrival("r", (3, 3)))
print(where_is_arrival("u", (3, 3)))
print(where_is_arrival("d", (3, 3)))
print(where_is_arrival("k", (3, 3)))


# And finally we have to make this mvt a reality -------------------------


def display_mvt(board, start_slot, end_slot):
    x1, y1 = start_slot
    x2, y2 = end_slot
    board[y1][x1] = 0  # leave previous slot
    board[y2][x2] = 2  # get to next slot
    return board


def actualise_player_pos(player_table, player_id, end_slot):
    player_table[player_id][2], player_table[player_id][3] = end_slot
    return player_table


# example
my_board = np.array(([0, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0]))
print(my_board)
print(display_mvt(my_board, (2, 0), (2, 1)))


# And there's the final moving function (very cool bcs it doesn't make you move if you do smth wrong)


def move(player_id, direction, world):
    player_table, board = world
    start_slot = player_table[player_id][2], player_table[player_id][3]
    end_slot = where_is_arrival(direction, start_slot)

    if i_can_move(end_slot, board):
        if there_is_food(end_slot, board):
            player_eats(player_table, player_id)
        board = display_mvt(board, start_slot, end_slot)
        player_table = actualise_player_pos(player_table, player_id, end_slot)
        print(board)
        print(player_table)
    return player_table, board


# example :
my_world = create_world(10, 5, 6, 3)
print("-----------------------")
print(my_world[0])
print(my_world[1])
my_world = move(0, "d", my_world)
my_world = move(0, "l", my_world)


# Now let's automate this game, it's quite tedious to have to control every player =====================================

# We will define one 'turn' by each player moving once randomly ('random') or controlled by a real person ('real')

def random_turn(world):
    player_table, board = world
    for player_id in range(len(player_table)):
        direction = random.choice(possible_directions)
        world = move(player_id, direction, world)
    return world


def real_turn(world):
    player_table, board = world
    for player_id in range(len(player_table)):
        while True:
            direction = input('In which direction does player ' + str(player_id) + ' want to go ?')
            if direction in possible_directions:
                break
            else:
                print('This is not a valid direction.')
        world = move(player_id, direction, world)
    return world


def next_turn(type_of_player, world):
    if type_of_player == 'random':
        world = random_turn(world)
    elif type_of_player == 'real':
        world = real_turn(world)
    return world


# example :
my_world = create_world(4, 4, 2, 2)
print(my_world[0], my_world[1])
next_turn('real', my_world)


# Let's measure the distance from any slot to the nearest food

def find_nearest_food(slot, board):
    x, y = slot
    for i in range(max(get_dimensions(board))):


