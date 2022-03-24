import pathlib

INPUT = pathlib.Path(__file__).parent / "input.txt"

PAIRS = {"(":")",
         "[":"]",
         "{":"}",
         "<":">"
         }

def load_input(file=INPUT):
    lines = open(file, "r").read().splitlines()
    return lines

def is_corrupted(chunk):
    stack=""
    for c in chunk:
        

def part1(file=INPUT):
    return


def part2(file=INPUT):
    return


if __name__ == "__main__":
    print(part1())

