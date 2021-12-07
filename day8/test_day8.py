from pytest import fixture
import pathlib
import main

TEST_INPUT = pathlib.Path(__file__).parent / "test_input.txt"


@fixture
def input():
    return main.load_input(TEST_INPUT)


def test_load_input(input):
    expected = 
    assert input == expected
