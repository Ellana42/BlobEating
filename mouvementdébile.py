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
     
         #Mouvement qui prend en compte les murs (i.e. les bords du plateau et les autres joueurs
   
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
    
    def there_is_no_player(self, x, y):
        cell_content = self.board[y][x]
        return not (World.RANGE_PLAYER <= cell_content < World.RANGE_END)

    def i_can_move(self, end_slot):
        x, y = end_slot
        return self.is_on_the_board(x, y) and self.there_is_no_player(x, y)

     
    def direction_choice(self):  
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

   