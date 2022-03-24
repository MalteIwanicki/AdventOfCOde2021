from pytest import fixture
import pathlib
import main

TEST_INPUT = pathlib.Path(__file__).parent / "test_input.txt"


@fixture
def input():
    return main.load_input(TEST_INPUT)


def test_load_input(input):
    expected = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]
    assert input == expected


def test_is_corrupted():
    corrupted_chunks = ["(]", "{()()()>", "(((()))}", "<([]){()}[{}])"]
    for chunk in corrupted_chunks:
        assert main.is_corrupted(chunk)


# def test_part1():
#     assert main.part1(TEST_INPUT) == 15


# def test_part2():
#     assert main.part2(TEST_INPUT) == 1134
