from pathlib import Path


class LdrModel:
    def __init__(self, path: Path):
        self.name = path.name
