import numpy as np
import pytest

from pyldraw.brick import Brick
from pyldraw.brick import BrickFactory as Factory


def test_brick_default_name():
    default_brick = Brick()
    assert default_brick.name == ""


def test_brick_default_position_at_origin():
    default_brick = Brick()
    assert default_brick.position == [0, 0, 0]


def test_brick_default_orientation():
    default_brick = Brick()
    np.testing.assert_array_equal(default_brick.orientation, np.eye(3))


def test_brick_default_color():
    default_brick = Brick()
    assert default_brick.color == 16


def test_bricks_with_same_data_are_same():
    brick1 = Brick()
    brick2 = Brick()
    assert brick1 == brick2


def test_brick_has_reproducible_hash():
    hash1 = hash(Brick())
    assert hash1 == hash(Brick())


def test_brick_hash_is_unique_on_name():
    hash1 = hash(Brick(name="foo"))
    assert hash1 != hash(Brick(name="bar"))


def test_brick_hash_is_unique_on_position():
    hash1 = hash(Brick(position=[3, 2, 1]))
    assert hash1 != hash(Brick(position=[1, 2, 3]))


def test_brick_print_info():
    brick = Brick()
    assert str(brick) == "Name: \nPosition:\n X : 0, Y : 0, Z : 0"


@pytest.mark.parametrize(
    "input_kwargs,expected",
    [
        (dict(color=15), "15 0 0 0 1 0 0 0 1 0 0 0 1"),
        (dict(position=[0.1, 0.2, 0.3]), "16 0.1 0.2 0.3 1 0 0 0 1 0 0 0 1"),
        (
            dict(orientation=np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5.6]])),
            "16 0 0 0 1 2 3 2 3 4 3 4 5.6",
        ),
    ],
)
def test_brick_repr_info(input_kwargs, expected):
    brick = Brick(name="brick", **input_kwargs)
    assert repr(brick) == f"1 {expected} brick.dat"


def test_brick_factory():
    result = Factory.gen("15 0 0 0 1 0 0 0 1 0 0 0 1 brick.dat")
    assert isinstance(result, Brick)


@pytest.mark.parametrize(
    "position,expected",
    [
        ("1 2 3", [1, 2, 3]),
        ("1.0 2.0 3.0", [1, 2, 3]),
        ("1.2 3.4 5.6", [1.2, 3.4, 5.6]),
    ],
)
def test_brick_factory_set_position(position, expected):
    result = Factory.gen(f"15 {position} 1 0 0 0 1 0 0 0 1 brick.dat")
    assert result.position == expected


@pytest.mark.parametrize(
    "orientation,expected",
    [
        ("1 2 3 2 3 4 3 4 5", [[1, 2, 3], [2, 3, 4], [3, 4, 5]]),
        ("1 2 3 2 3 4 3 4 5.0", [[1, 2, 3], [2, 3, 4], [3, 4, 5]]),
    ],
)
def test_brick_factory_set_orientation(orientation, expected):
    result = Factory.gen(f"15 0 0 0 {orientation} brick.dat")
    expected = np.array(expected)
    np.testing.assert_array_equal(result.orientation, expected)


def test_brick_factory_set_names():
    result = Factory.gen("15 1 2 3 1 2 3 2 3 4 3 4 5 brick.dat")
    assert result.name == "brick"
