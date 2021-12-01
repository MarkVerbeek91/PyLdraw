from pathlib import Path

from pyldraw.brick import Brick
from pyldraw.pyldraw import LdrModel

terrain = LdrModel(Path('terrain.ldr'))

for i in range(6):
    brick = Brick(name='brick.ldr', position=[i, 0, 0])
    terrain.add(brick)

if __name__ == "__main__":
    terrain.save(Path('tmp', 'terrain.ldr'))
