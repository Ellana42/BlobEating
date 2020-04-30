class Display:
    def __init__(self, world):
        self.world = world
        self.food_icon = ' #'
        self.blob_icon = ' 2'
        self.empty_space = '  '

    def display(self):
        w, h = self.world.get_dimensions()

        print('_' * 2 * (w + 1))
        for y in range(h):
            print("|", end='')
            for x in range(w):
                if (x, y) in self.world.food:
                    print(self.food_icon, end='')
                elif (x, y) in self.world.get_blob_positions():
                    print(self.blob_icon, end='')
                else:
                    print(self.empty_space, end='')
            print("|")

        print('-' * (w + 1) * 2)
