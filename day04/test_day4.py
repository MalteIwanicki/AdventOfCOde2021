from pytest import fixture
import pathlib
import main

TEST_FILE = pathlib.Path(__file__).parent / "test_input.txt"


def test_part1():
    assert main.part1(TEST_FILE) == 4512


def test_part2():
    assert main.part2(TEST_FILE) == 1924


def test_read_input_numbers():
    expected_numbers = [
        "7",
        "4",
        "9",
        "5",
        "11",
        "17",
        "23",
        "2",
        "0",
        "14",
        "21",
        "24",
        "10",
        "16",
        "13",
        "6",
        "15",
        "25",
        "12",
        "22",
        "18",
        "20",
        "8",
        "19",
        "3",
        "26",
        "1",
    ]
    numbers, _ = main.read_input_numbers_and_bingo_tables(TEST_FILE)
    assert numbers == expected_numbers


def test_read_bingo_tables():
    expected_tables = [
        [
            ["22", "13", "17", "11", "0"],
            ["8", "2", "23", "4", "24"],
            ["21", "9", "14", "16", "7"],
            ["6", "10", "3", "18", "5"],
            ["1", "12", "20", "15", "19"],
        ],
        [
            ["3", "15", "0", "2", "22"],
            ["9", "18", "13", "17", "5"],
            ["19", "8", "7", "25", "23"],
            ["20", "11", "10", "24", "4"],
            ["14", "21", "16", "12", "6"],
        ],
        [
            ["14", "21", "17", "24", "4"],
            ["10", "16", "15", "9", "19"],
            ["18", "8", "23", "26", "20"],
            ["22", "11", "13", "6", "5"],
            ["2", "0", "12", "3", "7"],
        ],
    ]
    _, tables = main.read_input_numbers_and_bingo_tables(TEST_FILE)
    assert tables == expected_tables


def test_sum_of_unmarked_numbers():
    table = [
        ["-14", "-21", "-17", "-24", "-4"],
        ["10", "16", "15", "-9", "19"],
        ["18", "8", "-23", "26", "20"],
        ["22", "-11", "13", "6", "-5"],
        ["-2", "-0", "12", "3", "-7"],
    ]
    sum = main.sum_of_unmarked_numbers(table)
    expected = 188
    assert sum == expected


def test_final_score():
    assert main.final_score(188, 24) == 4512


def test_call_numbers():
    _, tables = main.read_input_numbers_and_bingo_tables(TEST_FILE)
    main.call_number("7", tables)
    expected_result = [
        [
            ["22", "13", "17", "11", "0"],
            ["8", "2", "23", "4", "24"],
            ["21", "9", "14", "16", "-7"],
            ["6", "10", "3", "18", "5"],
            ["1", "12", "20", "15", "19"],
        ],
        [
            ["3", "15", "0", "2", "22"],
            ["9", "18", "13", "17", "5"],
            ["19", "8", "-7", "25", "23"],
            ["20", "11", "10", "24", "4"],
            ["14", "21", "16", "12", "6"],
        ],
        [
            ["14", "21", "17", "24", "4"],
            ["10", "16", "15", "9", "19"],
            ["18", "8", "23", "26", "20"],
            ["22", "11", "13", "6", "5"],
            ["2", "0", "12", "3", "-7"],
        ],
    ]
    assert tables == expected_result


def test_get_winner_table():
    _, tables = main.read_input_numbers_and_bingo_tables(TEST_FILE)
    nums = ["7", "4", "9", "5", "11", "17", "23", "2", "0", "14", "21"]
    for num in nums:
        main.call_number(num, tables)
    assert not main.get_winning_table(tables)
    main.call_number("24", tables)
    expected_winner = [
        ["-14", "-21", "-17", "-24", "-4"],
        ["10", "16", "15", "-9", "19"],
        ["18", "8", "-23", "26", "20"],
        ["22", "-11", "13", "6", "-5"],
        ["-2", "-0", "12", "3", "-7"],
    ]
    assert main.get_winning_table(tables) == expected_winner

