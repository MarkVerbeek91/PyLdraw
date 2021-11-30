from pathlib import Path

from pyldraw.pyldraw import LdrModel


def test_ldraw_object():
    LdrModel(Path())


def test_ldr_model_get_file_name():
    path = Path(__file__) / 'data' / 'single_brick.ldr'
    model = LdrModel(path)
    assert model.name == 'single_brick.ldr'
