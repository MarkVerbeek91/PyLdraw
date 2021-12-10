import re

from pyldraw.brick import BrickFactory


def parser(data):
    result = {}

    for line in data:
        parts = [part for part in re.split("\\s+", line) if part != ":"]
        if is_special_line(parts):
            process_special_line(parts, result)
        elif is_ldr_line(parts):
            add_brick(parts, result)
    return result


def process_special_line(parts, result):
    if is_file_keyword(parts):
        set_name(parts, result)
    elif "author" in parts[1].lower():
        result["Author"] = parts[2]


def set_name(parts, result):
    result["name"] = parts[-1].split(".")[0]


def is_file_keyword(parts):
    return parts[1].upper() == "FILE"


def add_brick(parts, result):
    brick = BrickFactory.gen(" ".join(parts[1:]))
    result.setdefault("bricks", []).append(brick)


def is_ldr_line(parts):
    return parts[0] == "1"


def is_special_line(parts):
    return parts[0] == "0"
