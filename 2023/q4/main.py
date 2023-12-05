def run_pt_1():
    total = 0
    with open("inputs.txt", "r") as f:
        for line in f:
            if line == "\n":
                continue

            num = _q1_logic(line)

            total += num

    print(total)


def _q1_logic(line):
    card = line.split(":")

    nums = card[1].split("|")

    win_nums = nums[0].split()
    my_nums = nums[1].split()

    wins = 0

    for num in win_nums:
        if num in my_nums:
            wins += 1

    x = {
        0: 0,
        1: 1,
        2: 2,
        3: 4,
        4: 8,
        5: 16,
        6: 32,
        7: 64,
        8: 128,
        9: 256,
        10: 512,
        11: 1024,
        12: 2048,
        13: 4096,
        14: 8192,
    }

    return x[wins]


def run_pt_2():
    total = 0

    scratch_card_count = {}
    with open("inputs.txt", "r") as f:
        for line in f:
            if line == "\n":
                continue

            scratch_card_count = q2_logic(line, scratch_card_count)

    print(sum(list(scratch_card_count.values())))


def q2_logic(line, scratch_card_count):
    card = line.split(":")

    card_num = int(card[0].split()[1])

    if card_num not in scratch_card_count:
        scratch_card_count[card_num] = 1
    else:
        scratch_card_count[card_num] += 1

    nums = card[1].split("|")

    win_nums = nums[0].split()
    my_nums = nums[1].split()

    wins = 0

    for num in win_nums:
        if num in my_nums:
            wins += 1

    win_multiplier = scratch_card_count[card_num]

    for i in range(wins):
        win_num = i + 1

        if card_num + win_num not in scratch_card_count:
            scratch_card_count[card_num + win_num] = 1 * win_multiplier
        else:
            scratch_card_count[card_num + win_num] += 1 * win_multiplier

    return scratch_card_count


if __name__ == "__main__":
    # run_pt_1()
    run_pt_2()
