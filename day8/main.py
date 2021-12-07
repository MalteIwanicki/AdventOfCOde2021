import pathlib

INPUT = pathlib.Path(__file__).parent / "input.txt"


def load_input(file=INPUT):
    lines = open(file, "r").read().splitlines()
    return [int(f) for f in lines[0].split(",")]

