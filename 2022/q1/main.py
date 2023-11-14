def run():
    top_elf = 0
    current_elf = 0
    with open("inputs.txt", "r") as f:
        for line in f:
            if line == "\n":
                if current_elf > top_elf:
                    top_elf = current_elf
                current_elf = 0
                continue

            current_elf += int(line)

    print(top_elf)


if __name__ == "__main__":
    run()
