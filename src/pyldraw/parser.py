import re

from pyldraw.brick import BrickFactory
from pyldraw.step import Step


class ParserError(Exception):
    """Error for when an illegal construction in LDR file is found"""


def parser(data):
    result = {}

    data_iter = iter(data)
    for line in data_iter:
        parts = [part for part in re.split("\\s+", line) if part != ":"]
        if is_special_line(parts):
            process_special_line(result, parts)
        elif is_ldr_line(parts):
            add_brick(result, parts)

    verify(result)

    return result


def process_special_line(result, parts):
    if is_file_keyword(parts):
        set_name(result, parts)
    elif "author" in parts[1].lower():
        result["Author"] = parts[2]
    elif "step" in parts[1].lower():
        result.setdefault("steps", []).append((Step()))


def add_brick(result, parts):
    brick = BrickFactory.gen(" ".join(parts[1:]))
    result.setdefault("bricks", []).append(brick)

    if "steps" in result:
        result["steps"][-1].append(brick)


def verify(result):
    def rule_steps_not_empty(x):
        for step in x.get("steps", []):
            if len(step) == 0:
                raise ParserError("step is empty")

    rule_steps_not_empty(result)


def set_name(result, parts):
    result["name"] = parts[-1].split(".")[0]


def is_file_keyword(parts):
    return parts[1].upper() == "FILE"


def is_ldr_line(parts):
    return parts[0] == "1"


def is_special_line(parts):
    return parts[0] == "0"
