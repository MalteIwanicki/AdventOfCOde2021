def part1(file):
    input_numbers, bingo_tables = read_input_numbers_and_bingo_tables(file)
    for num in input_numbers:
        call_number(num, bingo_tables)
        winner = get_winning_table(bingo_tables)
        if winner:
            return final_score(sum_of_unmarked_numbers(winner), int(num))


def part2(file):
    input_numbers, bingo_tables = read_input_numbers_and_bingo_tables(file)
    for num in input_numbers:
        call_number(num, bingo_tables)
        while True:
            winner = get_winning_table(bingo_tables)
            if winner:
                bingo_tables.remove(winner)
                if not bingo_tables:
                    return final_score(sum_of_unmarked_numbers(winner), int(num))
            else:
                break


def read_input_numbers_and_bingo_tables(file):
    lines = open(file, "r").read().splitlines()
    input_numbers = lines.pop(0).split(",")
    bingo_tables = []
    for line in lines:
        if not line:
            bingo_tables.append([])
            continue
        bingo_tables[-1].append(line.split())
    return input_numbers, bingo_tables


def sum_of_unmarked_numbers(table):
    sum = 0
    for row in table:
        for number in row:
            if not number.startswith("-"):
                sum += int(number)
    return sum


def call_number(called_num, bingo_tables):
    for i, table in enumerate(bingo_tables):
        for j, row in enumerate(table):
            for k, num in enumerate(row):
                if num == called_num:
                    bingo_tables[i][j][k] = "-" + num


def get_winning_table(tables):
    rows = 5
    columns = 5
    for table in tables:
        for row in range(rows):
            for col in range(columns):
                if not table[row][col].startswith("-"):
                    break
            else:
                return table
        for col in range(columns):
            for row in range(rows):
                if not table[row][col].startswith("-"):
                    break
            else:
                return table
    return None


def final_score(sum, last_called_number):
    return sum * int(last_called_number)


if __name__ == "__main__":
    print(part1("day4/input.txt"))
    print(part2("day4/input.txt"))

