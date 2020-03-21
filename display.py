class Display:
    def __init__(self, world):
        self.world = world
        self.food_icon = ' 1'
        self.blob_icon = ' 2'
        self.empty_space = '  '

    def display(self):
        w, h = self.world.get_dimensions()
        blob_positions = [(blob.x, blob.y) for blob in self.world.blobs.values()]

        print('_' * 2 * (w + 1))
        for y in range(h):
            print("|", end='')
            for x in range(w):
                if (x, y) in self.world.food:
                    print(self.food_icon, end='')
                elif (x, y) in blob_positions:
                    print(self.blob_icon, end='')
                else:
                    print(self.empty_space, end='')
            print("|")

        print('_' * (w + 1) * 2)

