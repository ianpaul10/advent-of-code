_symbols = "!@#$%^&*()_-+={}[]/\\|:;'<>,?/"  # not incl .

_symbols_arr = list(_symbols)


def run_pt_1():
    lines = []

    with open("inputs.txt", "r") as f:
        for line in f:
            if line == "\n":
                continue

            lines.append(line)

    total = _q1_logic_2(lines)
    print(total)


def _q1_logic_2(lines):
    total = 0

    for row_num, row in enumerate(lines):
        current_num_str = None
        current_num_touches_symbol = False

        for col_num, char in enumerate(row):
            if char.isdigit():
                if current_num_str is None:
                    current_num_str = char
                else:
                    current_num_str = current_num_str + char

                # check surrounding indexes for symbols
                if _touches_symbol_q1(lines, row_num, col_num):
                    current_num_touches_symbol = True
            else:
                # char is not a digit
                if current_num_str is not None and current_num_touches_symbol:
                    total += int(current_num_str)
                    current_num_str = None
                    current_num_touches_symbol = False

                current_num_str = None
                current_num_touches_symbol = False

    return total


def _q2_logic_2(lines):
    total = 0

    ast_coords_dict = {}

    for row_num, row in enumerate(lines):
        current_num_str = None
        current_num_touches_symbol = False
        ast_coords = None, None

        for col_num, char in enumerate(row):
            if char.isdigit():
                if current_num_str is None:
                    current_num_str = char
                else:
                    current_num_str = current_num_str + char

                # check surrounding indexes for symbols
                touches_symbol, symbol_row, symbol_col = _touches_symbol_q2(
                    lines, row_num, col_num, only_ast=True
                )

                if touches_symbol:
                    current_num_touches_symbol = True
                    ast_coords = symbol_row, symbol_col
            else:
                # char is not a digit
                if current_num_str is not None and current_num_touches_symbol:
                    # total += int(current_num_str)
                    if ast_coords not in ast_coords_dict:
                        ast_coords_dict[ast_coords] = [int(current_num_str)]
                    else:
                        ast_coords_dict[ast_coords].append(int(current_num_str))
                    current_num_str = None
                    current_num_touches_symbol = False

                current_num_str = None
                current_num_touches_symbol = False

    for ast_coords, nums in ast_coords_dict.items():
        if len(nums) == 2:
            total += nums[0] * nums[1]

    return total


def _touches_symbol_q1(lines, row_num, col_num, only_ast=False):
    # check current_row
    if _cell_is_symbol(lines, row_num, col_num - 1, only_ast=only_ast):
        return True
    if _cell_is_symbol(lines, row_num, col_num + 1, only_ast=only_ast):
        return True

    # check below
    if _cell_is_symbol(lines, row_num + 1, col_num, only_ast=only_ast):
        return True
    if _cell_is_symbol(lines, row_num + 1, col_num - 1, only_ast=only_ast):
        return True
    if _cell_is_symbol(lines, row_num + 1, col_num + 1, only_ast=only_ast):
        return True

    # check above
    if _cell_is_symbol(lines, row_num - 1, col_num, only_ast=only_ast):
        return True

    if _cell_is_symbol(lines, row_num - 1, col_num - 1, only_ast=only_ast):
        return True

    if _cell_is_symbol(lines, row_num - 1, col_num + 1, only_ast=only_ast):
        return True

    return False


def _touches_symbol_q2(lines, row_num, col_num, only_ast=False):
    # check current_row
    if _cell_is_symbol(lines, row_num, col_num - 1, only_ast=only_ast):
        return True, row_num, col_num - 1
    if _cell_is_symbol(lines, row_num, col_num + 1, only_ast=only_ast):
        return True, row_num, col_num + 1

    # check below
    if _cell_is_symbol(lines, row_num + 1, col_num, only_ast=only_ast):
        return True, row_num + 1, col_num
    if _cell_is_symbol(lines, row_num + 1, col_num - 1, only_ast=only_ast):
        return True, row_num + 1, col_num - 1
    if _cell_is_symbol(lines, row_num + 1, col_num + 1, only_ast=only_ast):
        return True, row_num + 1, col_num + 1

    # check above
    if _cell_is_symbol(lines, row_num - 1, col_num, only_ast=only_ast):
        return True, row_num - 1, col_num

    if _cell_is_symbol(lines, row_num - 1, col_num - 1, only_ast=only_ast):
        return True, row_num - 1, col_num - 1

    if _cell_is_symbol(lines, row_num - 1, col_num + 1, only_ast=only_ast):
        return True, row_num - 1, col_num + 1

    return False, None, None


def _cell_is_symbol(lines, row_num, col_num, only_ast=False):
    if row_num < 0 or row_num > len(lines) - 1:
        return False
    if col_num < 0 or col_num > len(lines[row_num]) - 1:
        return False

    if only_ast:
        return lines[row_num][col_num] == "*"

    return lines[row_num][col_num] in _symbols_arr


def run_pt_2():
    lines = []

    with open("inputs.txt", "r") as f:
        for line in f:
            if line == "\n":
                continue

            lines.append(line)

    total = _q2_logic_2(lines)
    print(total)


if __name__ == "__main__":
    # run_pt_1()
    run_pt_2()
