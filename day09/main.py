import pathlib

INPUT = pathlib.Path(__file__).parent / "input.txt"


def load_input(file=INPUT):
    lines = open(file, "r").read().splitlines()
    heatmap = []
    for line in lines:
        heatmap.append([int(h) for h in line])
    return heatmap


def get_risk_level(points, heatmap):
    point_values = 0
    for p in points:
        point_values += heatmap[p[0]][p[1]]
    return point_values + len(points)


def get_low_points(heatmap):
    hm = heatmap
    low_points = []
    for i in range(len(hm[0])):
        for j in range(len(hm)):
            neighbours = []
            if j != 0:
                neighbours.append(hm[j - 1][i])
            if j != len(hm) - 1:
                neighbours.append(hm[j + 1][i])
            if i != 0:
                neighbours.append(hm[j][i - 1])
            if i != len(hm[0]) - 1:
                neighbours.append(hm[j][i + 1])
            if hm[j][i] < min(neighbours):
                low_points.append((j, i))
    return low_points


def find_basins_sizes(low_points, heatmap):
    hm = heatmap
    for point in low_points:
        size = 1


def find_three_largest(list):
    three_largest = []
    for n in range(3):
        biggest = max(list)
        list.remove(biggest)
        three_largest.append(biggest)
    return three_largest


def get_score(list):
    result = 1
    for n in list:
        result = result * n
    return result


def part1(file=INPUT):
    heatmap = load_input(file)
    low_points = get_low_points(heatmap)
    return get_risk_level(low_points, heatmap)


def part2(file=INPUT):
    input = load_input(file)
    low_points = get_low_points(input)
    basinsizes = find_basins_sizes(input)


if __name__ == "__main__":
    print(part1())

