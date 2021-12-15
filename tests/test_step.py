from pyldraw.brick import Brick
from pyldraw.step import Step


def test_step_class():
    step = Step()
    assert len(step) == 0


def test_a_brick_can_be_added_to_step():
    step = Step()
    step.append(Brick())
    assert len(step) == 1
