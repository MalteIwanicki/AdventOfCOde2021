from pytest import fixture
import pathlib
import main

TEST_INPUT = pathlib.Path(__file__).parent / "test_input.txt"


@fixture
def crabs():
    return main.load_input(TEST_INPUT)


def test_load_input(crabs):
    expected = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert crabs == expected


def test_get_horizontal_and_fuel1(crabs):
    horizontal, fuel = main.get_horizontal_and_fuel_part1(crabs)
    expected_horizontal = 2
    expected_fuel = 37
    assert horizontal == expected_horizontal
    assert fuel == expected_fuel


def test_get_horizontal_and_fuel2(crabs):
    horizontal, fuel = main.get_horizontal_and_fuel_part2(crabs)
    expected_horizontal = 5
    expected_fuel = 168
    assert horizontal == expected_horizontal
    assert fuel == expected_fuel
