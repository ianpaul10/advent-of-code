_max_colour_count = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def run_pt_1():
    total = 0

    with open("inputs.txt", "r") as f:
        for line in f:
            if line == "\n":
                continue

            game_num, is_valid = _line_is_valid(line)

            if is_valid:
                total += game_num

    print(total)


def run_pt_2():
    total = 0

    with open("inputs_test.txt", "r") as f:
        for line in f:
            if line == "\n":
                continue

            amt = _pt_2_line_parse(line)

            total += amt

    print(total)


def _pt_2_line_parse(line: str):
    game_rounds = line.split(":")

    pulls = game_rounds[1].replace(";", ",").split(",")

    colour_max_count = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for pull in pulls:
        pull_pieces = pull.strip().split(" ")
        count = pull_pieces[0]
        colour = pull_pieces[1]

        count_int = int(count)

        if count_int > colour_max_count[colour]:
            colour_max_count[colour] = count_int

    return (
        colour_max_count["blue"] * colour_max_count["green"] * colour_max_count["red"]
    )


def _line_is_valid(line: str):
    game_rounds = line.split(":")

    game_num = int(game_rounds[0].split(" ")[1])

    pulls = game_rounds[1].replace(";", ",").split(",")

    for pull in pulls:
        pull_pieces = pull.strip().split(" ")
        count = pull_pieces[0]
        colour = pull_pieces[1]

        if int(count) > _max_colour_count[colour]:
            return game_num, False

    return game_num, True


if __name__ == "__main__":
    run_pt_2()
