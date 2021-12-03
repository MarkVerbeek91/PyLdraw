from pathlib import Path
from unittest import mock

import pytest

from pyldraw.brick import Brick
from pyldraw.pyldraw import LdrModel


def test_ldr_model_new_file():
    model = LdrModel(Path("brick"))
    assert model.name == "brick"
    assert isinstance(model.data, dict)


@pytest.fixture
def path_single_brick_model():
    return Path(__file__).parent / "data" / "single_brick.ldr"


@pytest.fixture
def path_multi_brick_model():
    return Path(__file__).parent / "data" / "multiple_bricks.ldr"


def test_ldr_model_get_file_name(path_single_brick_model):
    model = LdrModel(path_single_brick_model)
    assert model.name == "single_brick.ldr"


def test_ldr_model_has_length_one_as_minimum():
    assert len(LdrModel(Path())) == 1


def test_single_brick_ldr_model_is_initialised(path_single_brick_model):
    model = LdrModel(path_single_brick_model)
    assert len(model) == 1


def test_multiple_bricks_ldr_model_is_initialised(path_multi_brick_model):
    model = LdrModel(path_multi_brick_model)
    assert len(model) == 3


def test_empty_model_add_a_brick():
    model = LdrModel(Path("foo"))
    model.add(Brick(name="brick"))
    assert len(model) == 1


@pytest.fixture()
def single_brick(path_single_brick_model):
    with open(path_single_brick_model) as file_id:
        return file_id.read()


def test_save_to_file():
    model = LdrModel(Path("foo"))
    model.add(Brick(name="brick"))

    m = mock.mock_open()
    with mock.patch("builtins.open", m) as mock_file:
        model.save(Path())

    mock_file.assert_called_once_with(Path(), "w")


def test_repr_content_with_bricks(single_brick):
    model = LdrModel(Path("single_brick.ldr"))
    model.add(Brick(name="brick.ldr"))

    assert repr(model) == single_brick


def test_repr_content_as_import_model():
    model = LdrModel(Path("test_file.ldr"))
    assert repr(model) == "1 16 0 0 0 1 0 0 0 1 0 0 0 1 test_file.ldr"
