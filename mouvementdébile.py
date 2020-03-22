# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:14:24 2020

@author: jepiv
"""
import random
import numpy as np
from random import randrange, choice

class Blob:
    def __init__(self, x, y, blob_id):
        def __init__(self, x, y, blob_id, world):
          self.blob_id = blob_id
          self.x, self.y = x, y
          self.inventory = 0
          self.perception = None  
        
    def direction_choice(self):   #Mouvement complètement aléatoire
         direction = choice(['l', 'r', 'u', 'd'])
         return direction
     
        