import main
import pytest


@pytest.mark.parametrize(
        ('input_x', 'input_y', 'expected'),
        (
            (0, 0, 1),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 2)
        )
)
def test_foo(input_x, input_y, expected):
    '''assert main.foo(0, 0) == pytest.approx(1)
    assert pytest.approx(main.foo(1, 0)) == 1
    assert main.foo(0, 1) == 1
    assert main.foo(1, 1) == 2'''
    assert main.foo(input_x, input_y) == expected


@pytest.mark.parametrize(
        ('input_num', 'input_power', 'expected'),
        (
            (3, 2, 9),
            (2, 3, 8),
            (4, 3, 64)
        )
)
def test_bar(input_num, input_power, expected):
    #assert main.bar(3, 2) == 9
    assert main.bar(input_num, input_power) == expected
