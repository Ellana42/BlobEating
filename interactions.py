from world import World
from player import Blob
from game import Game
from random import choice
import numpy as np

choice = ['A','E'] #altruism or egoism

def generosity_matrix(self):
    pass

#Matrice de connectivité qui contiendra en coefficient(i,j) la probabilité que le blob i donne une unité de nourriture au blob j s'il peut le faire.


#Il faut ensuite stocker l'historique des décisions de chaque blob pour voir comment évoluent leurs décisions
def stock_decisions(self):
   for i in range (len(list_blobs)):
      list_decisions_i =[]

#ne coopère pas
def egoistic_blob(list_decisions_i, list_decisions_j):
    return 'E'

def altruistic_blob(list_decisions_i, list_decisions_j):
    return 'A'

#Donnant donnant
# coopère seulement si l'autre joueur a coopéré au coup précédent
def tit_for_tat(list_decisions_i, list_decisions_j):
    if len (list_decisions_j) >0:
      return list_decisions_j[-1]
  else : #premier tour
      return choice(choice)
      pass
