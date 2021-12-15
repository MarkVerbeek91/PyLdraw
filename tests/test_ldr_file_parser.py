from collections import Counter

import pytest

from pyldraw.brick import Brick
from pyldraw.parser import ParserError
from pyldraw.parser import parser as file_parser
from pyldraw.step import Step


def test_empty_file_is_empty_dict():
    assert file_parser([]) == {}


def test_comment_line_with_unknown_keyword_is_empty_dict():
    assert file_parser(["0 UNKNOWN"]) == {}


def test_comment_line_with_file_keyword_is_dict_with_name_keyword():
    assert file_parser(["0 FILE file_name.ldr"]) == {"name": "file_name"}


@pytest.mark.parametrize(
    "test_input",
    [
        "0 Author: LDraw",
        "0 Author : LDraw",
        "0 AutHOR : LDraw",
        "0  AutHOR  :  LDraw ",
    ],
)
def test_comment_line_with_author_line_is_dict_with_author_keyword(test_input):
    assert file_parser([test_input]) == {"Author": "LDraw"}


def test_comment_line_with_step_no_brick_line_result_in_error():
    line = ["0 STEP"]
    with pytest.raises(ParserError):
        file_parser(line)


def test_comment_line_with_step_keyword_add_next_brick_to_step(default_brick):
    line = ["0 STEP", default_brick]
    assert len(file_parser(line)["steps"]) == 1
    assert len(file_parser(line)["steps"][0]) == 1


def test_get_part_as_dict(default_brick):
    line = [default_brick]
    result = file_parser(line)
    assert Counter(result["bricks"]) == Counter([Brick(name="brick")])


def test_get_part_with_float_positions_as_dict():
    line = ["1 15 0.1 0.2 0.3 1 0 0 0 1 0 0 0 1 brick.ldr"]
    result = file_parser(line)
    assert Counter(result["bricks"]) == Counter(
        [Brick(name="brick", position=[0.1, 0.2, 0.3])]
    )


def test_get_multiple_parts_in_dict():
    lines = ["1 15 0 0 0 1 0 0 0 1 0 0 0 1 brick.ldr"] * 2
    result = file_parser(lines)
    assert Counter(result["bricks"]) == Counter(
        [Brick(name="brick"), Brick(name="brick")]
    )
