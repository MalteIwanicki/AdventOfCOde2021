def part1():
    power_consumption = lambda gamma, epsilon: gamma * epsilon
    gamma_rate = []
    epsilon_rate = []

    binaries = open("3/input.txt", "r").read().splitlines()

    tmp_rate = [0 for i in range(len(binaries[0]))]

    for binary in binaries:
        for i, b in enumerate(binary):
            tmp_rate[i] += 1 if int(b) == 1 else -1

    for i in range(len(tmp_rate)):
        gamma_rate.append("1" if tmp_rate[i] > 1 else "0")

    for num in gamma_rate:
        epsilon_rate.append("0" if int(num) == 1 else "1")

    epsilon_rate = "".join(epsilon_rate)
    gamma_rate = "".join(gamma_rate)

    return power_consumption(int(gamma_rate, 2), int(epsilon_rate, 2))


def part2(input):
    life_support_rating = lambda oxygen, c02: oxygen * c02
    binaries = get_binaries(input)
    return life_support_rating(
        get_value("oxygen", binaries), get_value("c02", binaries)
    )


def get_binaries(path):
    return open(path, "r").read().splitlines()


def get_value(oxygen_or_c02, binaries, bit_criteria=""):
    if oxygen_or_c02 == "c02":
        get_bit_criteria = lambda balance: "0" if balance < 0 else "1"
    else:
        get_bit_criteria = lambda balance: "1" if balance < 0 else "0"

    balance = 0
    for bin in binaries:
        bit = bin.replace(bit_criteria, "", 1)[0]
        balance += 1 if bit == "1" else -1
    bit_criteria += get_bit_criteria(balance)

    new_binaries = []
    for bin in binaries:
        if bin.startswith(bit_criteria):
            new_binaries.append(bin)

    if len(new_binaries) == 1:
        return int(new_binaries[0], 2)
    else:
        return get_value(oxygen_or_c02, new_binaries, bit_criteria)


if __name__ == "__main__":
    print(part2("day3/input.txt"))
