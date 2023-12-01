def run():
    elves = []
    top_elf = 0
    current_elf = 0
    with open("inputs.txt", "r") as f:
        for line in f:
            if line == "\n":
                elves.append(current_elf)
                if current_elf > top_elf:
                    top_elf = current_elf
                current_elf = 0
                continue

            current_elf += int(line)

    print(top_elf)

    elves.sort(reverse=True)
    print(elves[0] + elves[1] + elves[2])


if __name__ == "__main__":
    run()
