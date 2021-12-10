from pathlib import Path

from pyldraw.pyldraw import LdrModel

mars_rover = LdrModel(Path("references", "Lego_mars_rover.ldr"))

if __name__ == "__main__":
    mars_rover.save(Path("tmp", "mars_rover.ldr"))
