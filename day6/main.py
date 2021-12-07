def load_fish(file):
    lines = open(file, "r").read().splitlines()
    fish_as_list = [int(f) for f in lines[0].split(",")]
    return compress_fish(fish_as_list)


def compress_fish(list_with_fish):
    fish = [0 for _ in range(9)]
    for f in list_with_fish:
        fish[f] += 1
    return fish


def wait_days(fish, days):
    for day in range(days):
        new_fish = fish.pop(0)
        fish.append(new_fish)
        fish[6] += new_fish
    return fish


def amount_fish(fish):
    amount = 0
    for value in fish:
        amount += value
    return amount


def part1(file, days):
    fish = load_fish(file)
    fish = wait_days(fish, days)
    return amount_fish(fish)


if __name__ == "__main__":
    print(part1("day6/input.txt", 80))
    import timeit

    print(timeit.timeit(lambda: part1("day6/input.txt", 256), number=1))

