from world import World
from player import Blob
from game import Game
from random import *
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

choice = ['A', 'E']  # altruism or egoism

def generosity_matrix(M):


M = np.zeros((nb_blobs + 1, nb_blobs + 1))
  for k in range(nb_blobs):
    M[k, k + 1] = random()  # Génère un nombre aléatoire entre 0 et 1 ( une proba )
    M[k, 0] = random()
    M[K, K] = 1
return M
# Matrice de connectivité qui contiendra en coefficient(i,j) la probabilité que le blob i donne une unité de nourriture au blob j s'il peut le faire.

print (generosity_matrix(M))

# Le cas particulier de l'égoïsme total : cette matrice est une matrice identité de taille nb_blobs
M_egoism = np.identity(nb_blobs)

# En s'appuyant sur le principe d'une matrice de transition (d'ailleurs c'en est une), on peut calculer la probabilité qu'un blob donné ait coopéré k fois.
# Pour cela, il faut calculer cette matrice à la puissance n.

n = nb_turns  # ou nb_rounds ?

#---------- Calcul de la probabilité --------------- #
Iterated_matrix = np.round(linalg.matrix_power(generosity_matrix(
    M), np.int(n)), 4)  # Eleve la matrice a la puissance n, on arrondit
print("Matrice de connectivite pour k=" + str(k) +
      " elevee a la puissance n=" + str(n) + "")
print(Iterated_matrix)
roundish_proba = Iterated_matrix[0, k]         # On extrait le bon coefficient
print("La probabilite d'avoir au moins " + str(k) +
      " piles consecutifs avec " + str(n) + " lancers est " + str(roundish_proba))

# En utilisant pour chaque k la matrice de connectivité correspondante, on peut tracer en fonction de k la probabilité pour un blob de coopérer k fois consécutives
n = 100  # Nombre de tours
k = range(np.int(2 * np.log2(n))  # On prend k entre 0 et 2log(n) par exemple

#---------- Représentation graphique --------------- #

Proba_at_least_k=[]
for j in k:
  Iterated_matrix=linalg.matrix_power(generosity_matrix(k), np.int(n))
  Proba_at_least_k.append(Iterated_matrix[0, k])

plt.plot(Proba_at_least_k, 'o-')
plt.plot([np.log2(n), np.log2(n)], [0, 1], 'r--', label='Log_2(' + \
         str(n) + ') =' + str(np.round(np.log2(n), 2)) + ' ')
plt.xlabel('Entier $K$'), plt.ylabel('Probabilite'), plt.legend()
plt.title(
    'Probabilite de coopérer au moins $K$ fois consecutives avec ' + str(n) + ' tours')
plt.show()




# Ceci n'est peut être pas utile en fin de compte, à voir

# Il faut ensuite stocker l'historique des décisions de chaque blob pour voir comment évoluent leurs décisions
def stock_decisions(self):
   for i in range(nb_blobs):
      list_decisions_i=[]

# ne coopère pas
def egoistic_blob(list_decisions_i, list_decisions_j):
    return 'E'

def altruistic_blob(list_decisions_i, list_decisions_j):
    return 'A'



# Donnant donnant
# coopère seulement si l'autre joueur a coopéré au coup précédent
def tit_for_tat(list_decisions_i, list_decisions_j):
    if len(list_decisions_j) > 0:
      # On prend le dernier élément de la liste du joueur avec lequel on interagit
      return list_decisions_j[-1]
  else:  # premier tour, le choix est aléatoire et dépend des probabilités dans la matrice ci-dessus
      return choice(choice)
      pass
