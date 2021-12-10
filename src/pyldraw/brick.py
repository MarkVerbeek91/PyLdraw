import numpy as np


class Brick:
    def __init__(self, **kwargs):
        self.name = kwargs.pop("name", "")
        self.position = kwargs.pop("position", [0, 0, 0])
        self.orientation = kwargs.pop("orientation", np.eye(3, dtype=int))
        self.color = kwargs.pop("color", 16)

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.position == other.position
            and np.alltrue(self.orientation == other.orientation)
        )

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        position_string = ", ".join(
            [f"{p} : {l}" for p, l in zip(["X", "Y", "Z"], self.position)]
        )
        return f"Name: {self.name}\nPosition:\n {position_string}"

    def __repr__(self):
        position = " ".join([str(i) for i in self.position])
        orientation = " ".join([num2str(i) for i in self.orientation.flatten()])
        return f"1 {self.color} {position} {orientation} {self.name}"


def str2num(i):
    return float(i) if "." in i else int(i)


def num2str(i):
    return f"{i:g}"


class BrickFactory:
    @staticmethod
    def gen(data):
        elms = data.split(" ")
        brick_data = dict(
            color=elms[0],
            name=BrickFactory.get_name(elms[13]),
            position=BrickFactory.get_position(elms[1:4]),
            orientation=BrickFactory.get_orientation(elms[4:13]),
        )
        return Brick(**brick_data)

    @staticmethod
    def get_position(elms):
        return [str2num(i) for i in elms]

    @staticmethod
    def get_orientation(elms):
        rows = [row for row in BrickFactory.split_into_rows(elms)]
        return np.array([[str2num(i) for i in row] for row in rows])

    @staticmethod
    def split_into_rows(elms):
        for i in range(0, len(elms), 3):
            yield elms[i : i + 3]

    @staticmethod
    def get_name(elms):
        return elms.split(".")[0]
