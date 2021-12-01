from pathlib import Path
from pyldraw.parser import parser


class LdrModel:
    def __init__(self, path: Path):
        self.name = path.name
        self.data = {}
        self.parse_file_if_exist(path)

    def parse_file_if_exist(self, path):
        if path.is_file():
            with open(str(path), 'r') as file_id:
                data = file_id.read().split('\n')
            self.data = parser(data)

    def __len__(self):
        return len(self.data['bricks'])

    def __repr__(self):
        data = "\n".join([repr(brick) for brick in self.data['bricks']])
        repr_str = f"0 FILE {self.name}\n{data}"
        return repr_str

    def add(self, brick):
        self.data.setdefault('bricks', []).append(brick)

    def save(self, path):
        with open(path, 'w') as out_file:
            out_file.write(repr(self))
