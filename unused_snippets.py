# Function replaced by add_blobs(). Food is added at the beginning of each
# round.
# def create_world(self, food_quantity=5, nb_blobs=4):
#     self.add_food(food_quantity)
#     self.add_blobs(nb_blobs)


# Cette fonction n'est plus utilisée, en tout cas pour l'instant, parce
# qu'on a décidé de faire apparaître les blobs n'importe où sur le plateau
# plutôt qu'au bord.
# def random_border_tile(self):
#     w, h = self.width, self.height
#     while True:
#         borders = [(0, randrange(h)), (w - 1, randrange(h)),
#                    (randrange(w), 0), (randrange(w), h - 1)]
#         x, y = choice(borders)
#         if self.tile_is_empty(x, y):
#             return x, y
