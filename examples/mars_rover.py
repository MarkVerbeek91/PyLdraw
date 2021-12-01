from pathlib import Path

from pyldraw.brick import Brick
from pyldraw.pyldraw import LdrModel

from mars_terrain import terrain

mars_rover = LdrModel(Path('mars_rover'))
mars_rover.add(Brick(name='brick.ldr'))

rover_body = LdrModel(Path('rover_body.ldr'), position=[1, 2, 3])
mars_rover.add(rover_body)

terrain.position = [1, 3, 5]
mars_rover.add(terrain)

if __name__ == "__main__":
    mars_rover.save(Path('tmp', 'mars_rover.ldr'))

