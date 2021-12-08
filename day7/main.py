import pathlib

INPUT = pathlib.Path(__file__).parent / "input.txt"


def load_input(file):
    lines = open(file, "r").read().splitlines()
    return [int(f) for f in lines[0].split(",")]


def get_horizontal_and_fuel_part1(crabs):
    fuel_per_horizontal = {}
    for i in range(min(crabs), max(crabs) + 1):
        fuel = 0
        for c in crabs:
            fuel += abs(c - i)
        fuel_per_horizontal[i] = fuel

    best_horizontal = min(fuel_per_horizontal, key=fuel_per_horizontal.get)
    return best_horizontal, fuel_per_horizontal[best_horizontal]


def get_horizontal_and_fuel_part2(crabs):
    fuel_per_horizontal = {}
    for i in range(min(crabs), max(crabs) + 1):
        fuel = 0
        for c in crabs:
            n = dist = abs(c - i)
            fuel += (n * n + n) / 2  # gauss
            # fuel += sum(range(dist + 1))
        fuel_per_horizontal[i] = fuel

    best_horizontal = min(fuel_per_horizontal, key=fuel_per_horizontal.get)
    return best_horizontal, fuel_per_horizontal[best_horizontal]


def part1(file=INPUT):
    crabs = load_input(file)
    horizontal, fuel = get_horizontal_and_fuel_part1(crabs)
    return fuel


def part2(file=INPUT):
    crabs = load_input(file)
    horizontal, fuel = get_horizontal_and_fuel_part2(crabs)
    return fuel


if __name__ == "__main__":
    print(part1())
    print(part2())
