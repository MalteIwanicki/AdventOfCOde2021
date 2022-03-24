import pathlib

INPUT = pathlib.Path(__file__).parent / "input.txt"
ZERO = "abcefg", 0  # 6
ONE = "cf", 1  # 2
TWO = "acdeg", 2  # 5
THREE = "acdfg", 3  # 5
FOUR = "bcdf", 4  # 4
FIVE = "abdfg", 5  # 5
SIX = "abdefg", 6  # 6
SEVEN = "acf", 7  # 3
EIGHT = "abcdefg", 8  # 7
NINE = "abcdfg", 9  # 6
NUMBERS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]

A = "a"  # 8
B = "b"  # 6
C = "c"  # 8
D = "d"  # 7
E = "e"  # 5
F = "f"  # 9
G = "g"  # 7
ABCDEFG = [A, B, C, D, E, F, G]


def load_input(file=INPUT):
    lines = open(file, "r").read().splitlines()
    output = []
    for line in lines:
        keys, out = line.split(" | ")
        keys_ordered = ["".join(sorted(key)) for key in keys.split()]
        out_ordered = ["".join(sorted(out)) for out in out.split()]
        output.append({"keys": keys_ordered, "out": out_ordered})
    return output


def part1(file=INPUT):
    signals = load_input(file)
    count = 0
    for signal in signals:
        count += count_1_4_7_8(signal["out"])
    return count


def part2(file=INPUT):
    signals = load_input(file)
    return sum([get_sum(s) for s in signals])


def get_sum(dict):
    out = dict["out"]
    alphabet = define_alphabet(dict["keys"])
    number = ""
    for num in out:
        number += str(chars_to_number(alphabet, num))
    return int(number)


def count_1_4_7_8(signals):
    count = 0
    for s in signals:
        if (len(s) == 2) or (len(s) == 3) or (len(s) == 4) or (len(s) == 7):
            count += 1
    return count


def remove_chars(string, chars):
    for c in chars:
        string = string.replace(c, "")
    return string


def chars_in_string(string, chars):
    for c in chars:
        if not c in string:
            return False
    return True


def chars_to_number(dict, string):
    new_string = ""
    for s in string:
        for key, value in dict.items():
            if value == s:
                new_string += key
                break
    for number in NUMBERS:
        if not (len(number[0]) == len(new_string)):
            continue
        for c in number[0]:
            if not (c in new_string):
                break
        else:
            return number[1]
    pass


def define_alphabet(keys):
    alphabet = {
        "a": "",  #
        "b": "",  #
        "c": "",  #
        "d": "",
        "e": "",  #
        "f": "",  #
        "g": "",
        "ac": "",
        "dg": "",
    }
    all_chars = "".join([n for n in keys])
    for char in ABCDEFG:
        count = all_chars.count(char)
        if count == 4:
            alphabet["e"] = char
        elif count == 6:
            alphabet["b"] = char
        elif count == 7:
            alphabet["dg"] += char
        elif count == 8:
            alphabet["ac"] += char
        elif count == 9:
            alphabet["f"] = char

    alphabet["c"] = get_c(alphabet["f"], keys)
    alphabet["a"] = get_a(alphabet, keys)
    alphabet["d"], alphabet["g"] = get_d_g(alphabet, keys)

    del alphabet["dg"]
    return alphabet


def get_c(f_char, keys):
    for key in keys:
        if len(key) == 2:
            one = key
            break
    return remove_chars(one, f_char)


def get_a(alphabet, keys):
    for key in keys:
        if len(key) == 3:
            seven = key
            break
    return remove_chars(seven, alphabet["c"] + alphabet["f"])


def get_d_g(alphabet, keys):
    all_chars = ""
    for key in keys:
        if len(key) == 6:
            all_chars += key
    dg = alphabet["dg"]
    if all_chars.count(dg[0]) > all_chars.count(dg[1]):
        d = dg[1]
        g = dg[0]
    else:
        d = dg[0]
        g = dg[1]
    return d, g


def define_seven(dict):
    for key in dict["keys"]:
        if len(key) == 3:
            number = key
            break
    dict["seven"] = number
    dict["a"] = remove_chars(number, dict["one"])
    dict["keys"].remove(number)
    return dict


def define_four(dict):
    for key in dict["keys"]:
        if len(key) == 4:
            number = key
            break
    dict["four"] = number
    dict["bd"] = remove_chars(number, dict["one"])
    dict["keys"].remove(number)
    return dict


def define_nine(dict):
    possible_numbers = []
    for key in dict["keys"]:
        if len(key) == 6:
            possible_numbers.append(key)
    for num in possible_numbers:
        if chars_in_string(num, dict["one"] + dict["four"] + dict["seven"]):
            number = num
    dict["nine"] = number
    dict["g"] = remove_chars(number, dict["a"] + dict["cf"] + dict["bd"])
    dict["keys"].remove(number)
    return dict


def define_eight(dict):
    for key in dict["keys"]:
        if len(key) == 7:
            number = key

    dict["eight"] = number
    dict["e"] = remove_chars(number, dict["nine"])
    dict["keys"].remove(number)
    return dict


def define_six(dict):
    for num in dict["keys"]:
        if not (len(num) == 6):
            continue
        if chars_in_string(num, dict["bd"] + dict["e"]):
            number = num
            break
    dict["c"] = remove_chars("abcdefg", number)
    dict["f"] = dict["one"].replace(dict["c"], "")
    dict["six"] = number
    dict["keys"].remove(number)
    return dict


def define_zero(dict):
    for num in dict["keys"]:
        if not (len(num) == 6):
            continue
        if chars_in_string(num, dict["e"] + dict["f"] + dict["g"] + dict["c"]):
            number = num
            break
    dict["d"] = remove_chars("abcdefg", number)
    dict["b"] = dict["bd"].replace(dict["d"], "")
    dict["zero"] = number
    dict["keys"].remove(number)
    return dict


if __name__ == "__main__":
    print(part1())
    print(part2())
