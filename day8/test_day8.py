from pytest import fixture
import pathlib
from day8.main import get_sum
import main

TEST_INPUT = pathlib.Path(__file__).parent / "test_input.txt"
TEST_INPUT2 = pathlib.Path(__file__).parent / "test_input2.txt"


@fixture
def input():
    return main.load_input(TEST_INPUT)


def test_load_input(input):
    assert len(input) == 11
    expected = {
        "keys": [
            "be",
            "abcdefg",
            "bcdefg",
            "acdefg",
            "bceg",
            "cdefg",
            "abdefg",
            "bcdef",
            "abcdf",
            "bde",
        ],
        "out": ["abcdefg", "bcdef", "bcdefg", "bceg"],
    }

    assert input[0] == expected


def test_define_alphabet(input):
    dict = main.define_alphabet(input[1]["keys"])
    assert dict["a"] == "d"
    assert dict["b"] == "e"
    assert dict["c"] == "a"
    assert dict["d"] == "f"
    assert dict["e"] == "g"
    assert dict["f"] == "b"
    assert dict["g"] == "c"


def test_get_sum(input):
    assert get_sum(input[1]) == 5353


def test_part1():
    result = main.part1(TEST_INPUT)
    expected = 26
    assert result == expected


def test_part2():
    result = main.part2(TEST_INPUT)
    expected = 61229
