from pytest import fixture
from day3 import part2, get_binaries, get_value


TEST_DATA = "day3/test.txt"


def test_part2():
    assert part2(TEST_DATA) == 230


@fixture
def binaries():
    return get_binaries(TEST_DATA)


def test_get_binaries(binaries):
    assert binaries == [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


def test_get_value_oxygen(binaries):
    assert get_value("oxygen", binaries) == 10


def test_get_value_c02(binaries):
    assert get_value("c02", binaries) == 23
