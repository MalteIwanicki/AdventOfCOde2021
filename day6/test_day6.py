from pytest import fixture
from day5.test_day5 import TEST_DATA
import main

TEST_DATA = "day6/test_input.txt"


@fixture
def fish():
    return main.load_fish(TEST_DATA)


def test_load_fish(fish):
    expected = [0, 1, 1, 2, 1, 0, 0, 0, 0]
    assert fish == expected


def test_amount_fish(fish):
    expected = 5
    assert main.amount_fish(fish) == expected


def test_wait_days_1(fish):
    expected = main.compress_fish([2, 3, 2, 0, 1])
    fish = main.wait_days(fish, 1)
    assert fish == expected


def test_wait_days_2(fish):
    expected = main.compress_fish([1, 2, 1, 6, 0, 8])
    fish = main.wait_days(fish, 2)
    assert fish == expected


def test_compress_fish():
    res = main.compress_fish([0, 1, 1, 1, 2, 3, 6, 7, 8])
    exp = [1, 3, 1, 1, 0, 0, 1, 1, 1]
    assert res == exp


def test_part1():
    result = main.part1(TEST_DATA, 80)
    expected = 5934
    assert result == expected


def test_day_256(fish):
    fish = main.wait_days(fish, 256)
    expected = 26984457539
    assert main.amount_fish(fish) == expected


def test_part2():
    result = main.part1("day6/input.txt", 256)
    expected = 1682576647495
    assert result == expected
