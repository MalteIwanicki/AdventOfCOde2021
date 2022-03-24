from pytest import fixture
import pathlib
import main

TEST_INPUT = pathlib.Path(__file__).parent / "test_input.txt"


@fixture
def input():
    return main.load_input(TEST_INPUT)


def test_load_input(input):
    expected = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]
    assert input == expected


def test_get_low_points(input):
    assert 4 == len(main.get_low_points(input))


def test_risk_level(input):
    low_points = main.get_low_points(input)
    risk_level = main.get_risk_level(low_points, input)
    assert risk_level == 15


def test_part1():
    assert main.part1(TEST_INPUT) == 15


# TODO
# def test_part2():
#     assert main.part2(TEST_INPUT) == 1134


def test_find_three_largest():
    assert main.find_three_largest([3, 6, 8, 1, 9, 12]) == [12, 9, 8]


def test_get_score():
    assert main.get_score([14, 9, 9]) == 1134
