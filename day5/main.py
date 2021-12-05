def part1(file):
    coordinates = get_coordinates(file)
    display = initiate_display(coordinates)
    display, _ = draw_horizontal_lines(display, coordinates)
    return get_overlapping_score(display)


def part2(file):
    coordinates = get_coordinates(file)
    display = initiate_display(coordinates)
    display, coordinates = draw_horizontal_lines(display, coordinates)
    display, _ = draw_diagonal_lines(display, coordinates)
    return get_overlapping_score(display)


def get_coordinates(file):
    lines = open(file, "r").read().splitlines()
    coordinates = []
    for line in lines:
        numbers_as_strings = line.replace(" -> ", ",").split(",")
        numbers = [int(c) for c in numbers_as_strings]
        coordinates.append(tuple(numbers))
    return coordinates


def initiate_display(coordinates):
    size = 0
    for c in coordinates:
        size = max(size, max(c[0], c[1], c[2], c[3]))
    line = lambda: [0 for x in range(size + 1)]
    return [line() for y in range(size + 1)]


def draw_diagonal_lines(display, coordinates):
    remaining_coordinates = []
    for c in coordinates:
        if not (abs(c[0] - c[2]) == abs(c[1] - c[3])):
            remaining_coordinates.append(c)
        elif c[0] > c[2]:  # left
            if c[1] < c[3]:  # down
                for of in range(c[0] - c[2] + 1):
                    display[c[1] + of][c[0] - of] += 1
            else:  # up
                for of in range(c[0] - c[2] + 1):
                    display[c[1] - of][c[0] - of] += 1
        elif c[0] < c[2]:  # right
            if c[1] < c[3]:  # down
                for of in range(c[2] - c[0] + 1):
                    display[c[1] + of][c[0] + of] += 1
            else:  # up
                for of in range(c[2] - c[0] + 1):
                    display[c[1] - of][c[0] + of] += 1
    return display, remaining_coordinates


def draw_horizontal_lines(display, coordinates):
    remaining_coordinates = []
    for c in coordinates:
        if (c[0] == c[2]) or (c[1] == c[3]):
            for y in range(min(c[1], c[3]), max(c[1], c[3]) + 1):
                for x in range(min(c[0], c[2]), max(c[0], c[2]) + 1):
                    display[y][x] += 1
        else:
            remaining_coordinates.append(c)
    return display, remaining_coordinates


def get_overlapping_score(display):
    max_value = 0
    for row in display:
        for v in row:
            max_value = max(max_value, v)
    count = 0
    for row in display:
        for v in row:
            count += 1 if v >= 2 else 0
    return count


if __name__ == "__main__":
    print(part1("day5/input.txt"))
    print(part2("day5/input.txt"))
