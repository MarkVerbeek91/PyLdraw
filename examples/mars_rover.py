from pathlib import Path

from pyldraw.brick import Brick
from pyldraw.pyldraw import LdrModel

mars_rover = LdrModel(Path('mars_rover'))

mars_rover.add(Brick(name='brick.ldr'))

mars_rover.save(Path('tmp', 'mars_rover.ldr'))

