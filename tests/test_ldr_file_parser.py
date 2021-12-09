from collections import Counter

import pytest

from pyldraw.brick import Brick
from pyldraw.parser import parser


def test_get_file_as_dict():
    line = ["0 FILE file_name.ldr"]
    result = parser(line)
    assert result == {"name": "file_name"}


def test_process_special_line():
    line = ["0 UNKNOWN"]
    result = parser(line)
    assert result == {}


def test_get_part_as_dict():
    line = ["1 15 0 0 0 1 0 0 0 1 0 0 0 1 brick.ldr"]
    result = parser(line)
    assert "bricks" in result
    list_same = Counter(result["bricks"]) == Counter([Brick(name="brick")])
    assert list_same


def test_get_multiple_parts_in_dict():
    lines = ["1 15 0 0 0 1 0 0 0 1 0 0 0 1 brick.ldr"] * 2
    result = parser(lines)
    list_same = Counter(result["bricks"]) == Counter(
        [Brick(name="brick"), Brick(name="brick")]
    )
    assert list_same
