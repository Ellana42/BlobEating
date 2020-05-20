# Règles du jeu

### 1. Règles générales
1) Des blobs sont sur un plateau.

2) Une partie se déroule en un certain nombre de tours (rounds).

3) Au début de chaque tour, de la nourriture apparaît de manière aléatoire sur le plateau.

4) Au début de chaque tour, les blobs partent du bord du plateau, et peuvent se déplacer.

5) Les blobs ont un nombre de pas limités qu’ils peuvent faire en un tour.

6) Lorsqu'un blob arrive sur une case nourriture, il la met dans sa poche.

7) Si un blob termine un tour sans nourriture, il meurt.

8) Si un blob termine un tour avec au moins une unité de nourriture, il survit.

9) Si un blob termine un tour avec au moins deux unités de nourriture, il se reproduit.

10) Si un blob termine la partie avec plus de deux unités de nourriture, il peut en donner à d’autres blobs.

### 2. Entre chaque tour
1) les blobs qui ont plus de deux unités de nourriture donnent leurs unités en trop
2) les blobs qui ont au moins deux unités de nourriture se reproduisent.
3) les blobs qui n'ont pas de nourriture meurent.
4) la nourriture est effacée, et les blobs repartent au bord du plateau.

### 3. Modélisation des dons
La probabilité des dons peut être représentée par une matrice de connectivité, telle que, lorsque le blob i dispose d'une unité de nourriture excédentaire, le coefficient de coordonnées i,j est la probabilité que le blob i donne cette unité au blob j. Ainsi, si tous les blobs sont parfaitement égoïstes, la matrice de connectivité sera la matrice identité.

En pratique, dans le code, on peut avoir un vecteur de générosité comme attribut pour chaque blob.

La matrice de connectivité est initialisée, puis évolue comme ça :
1) Quand le blob i reçoit un don du blob j, la générosité du blob i envers le blob j augmente d'un certain coefficient (suggestion de nom : `gratefulness`)
2) Si le blob j a fait un don au blob i, et que le blob j ne reçoit pas de dons de i pendant un certain nombre de tours suivants, la générosité du blob j envers le blob i diminue d'un certain coefficient (suggestion de nom : `vexation`)

### 4. Reproduction
1) quand un blob se reproduit, un nouveau blob apparaît
2) Par défaut, ce nouveau blob a les mêmes caractéristiques (`gratefulness` et `vexation`) que son parent. Toutefois, il y a une probabilité que ces caractéristiques mutent (`mutation_probability`), c'est-à-dire qu'elles soient multipliée par un coefficient appelé `mutation_intensity`.
3) son vecteur de générosité est réinitialisé ( pour l'instant)
autres options envisagées : Ou le même que celui de son parent ? Avec une mutation ? Quelle est sa générosité envers son parent ?

### 5. Règles de déplacement
Les blobs vont vers la nourriture la plus proche.
