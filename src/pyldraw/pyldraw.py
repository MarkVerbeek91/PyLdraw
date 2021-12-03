from pathlib import Path

from pyldraw.brick import Brick
from pyldraw.parser import parser


class LdrModel(Brick):
    def __init__(self, path: Path, **kwargs):
        super(LdrModel, self).__init__(**kwargs)
        self.name = path.name
        self.data = {}
        self.parse_file_if_exist(path)

    def parse_file_if_exist(self, path):
        if path.is_file():
            with open(str(path), "r") as file_id:
                data = file_id.read().split("\n")
            self.data = parser(data)

    def __len__(self):
        return len(self.data.get("bricks", [1]))

    def __repr__(self):
        repr_str = (
            self.get_file_content() if "bricks" in self.data else self.get_file_import()
        )
        return repr_str

    def get_file_content(self):
        data = "\n".join([repr(brick) for brick in self.data["bricks"]])
        repr_str = f"0 FILE {self.name}\n{data}"
        return repr_str

    def get_file_import(self):
        return super().__repr__()

    def add(self, brick):
        self.data.setdefault("bricks", []).append(brick)

    def save(self, path):
        with open(path, "w") as out_file:
            out_file.write(repr(self))
