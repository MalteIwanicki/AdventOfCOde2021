from pytest import fixture
from day5.main import draw_horizontal_lines, part1
import main

TEST_DATA = "day5/test_input.txt"


@fixture
def coordinates():
    return main.get_coordinates(TEST_DATA)


def test_get_coordinates(coordinates):
    expected = [
        (0, 9, 5, 9),
        (8, 0, 0, 8),
        (9, 4, 3, 4),
        (2, 2, 2, 1),
        (7, 0, 7, 4),
        (6, 4, 2, 0),
        (0, 9, 2, 9),
        (3, 4, 1, 4),
        (0, 0, 8, 8),
        (5, 5, 8, 2),
    ]
    assert expected == coordinates


def test_initiate_display():
    coordinates = [(0, 1, 2, 3), (1, 1, 1, 1,), (3, 3, 3, 3)]
    result = main.initiate_display(coordinates)
    expected = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert result == expected


def test_draw_horizontal_lines(coordinates):
    display = main.initiate_display(coordinates)
    result, _ = main.draw_horizontal_lines(display, coordinates)
    expected = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
    ]
    assert result == expected


def test_draw_diagonal_lines(coordinates):
    display = main.initiate_display(coordinates)
    display, coordinates = main.draw_horizontal_lines(display, coordinates)
    result, _ = main.draw_diagonal_lines(display, coordinates)
    expected = [
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
        [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
        [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
        [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
    ]
    assert result == expected


def test_get_overlapping_score(coordinates):
    display = main.initiate_display(coordinates)
    display, _ = main.draw_horizontal_lines(display, coordinates)
    assert main.get_overlapping_score(display) == 5


def test_part1():
    assert main.part1(TEST_DATA) == 5


def test_part2():
    assert main.part2(TEST_DATA) == 12
