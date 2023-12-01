# https://adventofcode.com/2023/day/1


def run_pt_1():
    total = 0
    with open("inputs.txt", "r") as f:
        for line in f:
            if line == "\n":
                continue

            num = _extract_num(line)

            total += num

    print(total)


def _extract_num(line):
    line_chars = list(line)

    first_digit = ""
    last_digit = ""

    for i in line_chars:
        if i.isdigit():
            first_digit = i
            break

    for i in reversed(line_chars):
        if i.isdigit():
            last_digit = i
            break

    num = int(first_digit + last_digit)

    return num


def _extract_num_and_str(line, digits_str_to_int, reversed_digits_str_to_int):
    first_digit = _extract_num_and_str_with_dict(line, digits_str_to_int)

    last_digit = _extract_num_and_str_with_dict(line[::-1], reversed_digits_str_to_int)

    num = (first_digit * 10) + last_digit

    return num


def _extract_num_and_str_with_dict(line, digits_str_to_int):
    first_digit = 0
    first_digit_index = None

    for digit_str in digits_str_to_int.keys():
        try:
            digit_index = line.index(digit_str)
        except ValueError:
            continue

        if digit_index < first_digit_index or first_digit_index is None:
            first_digit_index = digit_index
            first_digit = digits_str_to_int[digit_str]

    return first_digit


def run_pt_2():
    total = 0

    digits_str_to_int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    reversed_digits_str_to_int = {}

    for k, v in digits_str_to_int.items():
        k = k[::-1]
        reversed_digits_str_to_int[k] = v

    with open("inputs.txt", "r") as f:
        for line in f:
            if line == "\n":
                continue

            num = _extract_num_and_str(
                line, digits_str_to_int, reversed_digits_str_to_int
            )

            total += num

    print(total)


if __name__ == "__main__":
    # run_pt_1()
    run_pt_2()
