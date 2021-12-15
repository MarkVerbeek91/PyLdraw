import sys

import pytest

sys.path.append("src")


@pytest.fixture
def default_brick():
    return "1 15 0 0 0 1 0 0 0 1 0 0 0 1 brick.ldr"
