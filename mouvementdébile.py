# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:14:24 2020

@author: jepiv
"""
import random
import numpy as np
from random import randrange, choice

class Player:
    def __init__(self, world, player_id, x, y):
        self.player_id = player_id
        self.x, self.y = x, y
        self.world = world
        self.food_inventory = 0
          
 class World:
    RANGE_FOOD = 1
    RANGE_PLAYER = 1000
    RANGE_END = 1999  
        
    def random_direction_choice(self):   #Mouvement complètement aléatoire
         direction = choice(['l', 'r', 'u', 'd'])
         return direction
    
    
   #Mouvement qui prend en compte les murs (i.e. les bords du plateau ) et les autres joueurs
   
    def where_is_arrival(self, direction):
        if direction not in "lrud":
            return None
        x, y = self.x, self.y
        dx, dy = {"l": (-1, 0), "r": (1, 0), "u": (0, -1), "d": (0, 1)}[direction]
        return x + dx, y + dy
    
    def set_pos(self, x, y):
        self.x, self.y = x, y

    def move(self, direction):
        where_to = self.where_is_arrival(direction)
        self.world.move_player(self.player_id, where_to)

    def is_on_the_board(self, x, y):
        return x in range(self.width) and y in range(self.height)
    
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
    
    def there_is_no_player(self, x, y):
        cell_content = self.board[y][x]
        return not (World.RANGE_PLAYER <= cell_content < World.RANGE_END)

    def i_can_move(self, end_slot):
        x, y = end_slot
        return self.is_on_the_board(x, y) and self.there_is_no_player(x, y)
  
    def direction_choice(self,direction):  
         direction = choice(['l', 'r', 'u', 'd'])
           if player_id not in self.players or end_slot is None or not self.i_can_move(end_slot):
            return False
            x, y = end_slot
            player = self.players[player_id]
            
      # On fait le déplacement sur le plateau
        self.board[y][x] = player_id
        self.board[player.y][player.x] = 0
        # on met à jour l'état du joueur
        player.set_pos(x, y)



     #Mouvement motivé par la nourriture
     
    class Food:
    def __init__(self, world, food_id, x, y, quantity=1):
        self.food_id = food_id
        self.x, self.y = x, y
        self.world = world
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

   def tile_is_empty(self, x, y):
        if not self.is_on_the_board(x, y):
            return False
        return self.board[y][x] == 0

    def random_empty_tile(self):
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
                raise ('Impossible to add food')
            food = Food(self, food_id, x, y)
            self.food[food_id] = food
            self.board[y][x] = food_id + World.RANGE_FOOD
     
    def hungry_player_movement(self):
          if player_id not in self.players or end_slot is None or not self.i_can_move(end_slot):
            return False
        x, y = end_slot
        player = self.players[player_id]
        if self.there_is_food(end_slot):
            food_id = self.board[y][x] - World.RANGE_FOOD
            if food_id in self.food:  # normalement, c'est toujours vrai
                # le joueur mange la nourriture
                player.eat(self.food[food_id])
                # on enleve la nourriture de la liste
                del self.food[food_id]
            else:
                raise("WRONG FOOD ID")
        # On fait le déplacement sur le plateau
        self.board[y][x] = player_id
        self.board[player.y][player.x] = 0
        # on met à jour l'état du joueur
        player.set_pos(x, y)
