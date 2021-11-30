import pytest
from collections import Counter

from pyldraw.parser import parser
from pyldraw.brick import Brick


def test_get_file_as_dict():
    line = ['0 FILE file_name.ldr']
    result = parser(line)
    assert result == {'name': 'file_name'}


def test_get_part_as_dict():
    line = ['1 15 0 0 0 1 0 0 0 1 0 0 0 1 brick.ldr']
    result = parser(line)
    assert 'bricks' in result
    list_same = Counter(result['bricks']) == Counter([Brick(name='brick')])
    assert list_same
