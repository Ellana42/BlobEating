from world import World
from display import Display

world = World()
world.create_world()
Display(world).display()

# Test

my_blob_id = 0

world.move_blob(blob_id=my_blob_id, direction='u')
Display(world).display()
world.move_blob(blob_id=my_blob_id, direction='u')
Display(world).display()
world.move_blob(blob_id=my_blob_id, direction='l')
Display(world).display()
world.move_blob(blob_id=my_blob_id, direction='l')
Display(world).display()
