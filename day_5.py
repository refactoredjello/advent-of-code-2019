class ProgramState:
    def __init__(self, int_codes, input):
        self.int_codes = int_codes
        self.input = input

    def set_value(self, idx, val):
        self.int_codes[int(idx)] = str(val)

    def set_input_at_pos(self, idx):
        self.set_value(int(self.int_codes[idx + 1]), self.input)

    def output(self, idx, mode):
        lookup = self.param_mode_handler(mode, idx + 1)
        print(f"out: {lookup}")
        if lookup != '0':
            print(f"debug idx {idx}, mode {mode}")
            print(f"out: {lookup}")

    def add(self, a, b, set_idx):
        val = a + b
        self.set_value(set_idx, val)

    def multiply(self, a, b, set_idx):
        val = a * b
        self.set_value(set_idx, val)

    def param_mode_handler(self, mode, idx):
        val = int(self.int_codes[idx])

        if mode == '0':
            return str(self.int_codes[val])

        return str(val)


def get_int_codes_from_file():
    with open('input_day_5.txt', 'r') as f:
        input = f.read()
        int_codes = [val for val in input.split(',')]

    return int_codes


def run_program(state):
    print(state.int_codes)
    pointer = 0

    while True:
        instructions = state.int_codes[pointer]
        if len(instructions) < 5:
            fill = '0' * (5 - len(instructions))
            instructions = fill + instructions

        optcode = instructions[-1]
        params_modes = instructions[:3]
        if optcode == '99':
            return state.int_codes[0]
        if optcode == '3':
            state.set_input_at_pos(pointer)
            pointer += 2
            continue
        if optcode == '4':
            state.output(pointer, params_modes[2])
            pointer += 2
            continue

        a = int(state.param_mode_handler(params_modes[2], pointer + 1))
        b = int(state.param_mode_handler(params_modes[1], pointer + 2))
        store_loc = int(state.int_codes[pointer + 3])

        if optcode == '1':
            state.add(a, b, store_loc)
            pointer += 4
            continue
        if optcode == '2':
            state.multiply(a, b, store_loc)
            pointer += 4
            continue


##
# Part 1
##
def part_1():
    int_codes = get_int_codes_from_file()
    s = ProgramState(int_codes, 1)
    return run_program(s)

part_1()

##
#Part 2
##
def run_program_part_two(state):
    print(state.int_codes)
    pointer = 0

    while True:
        instructions = state.int_codes[pointer]
        if len(instructions) < 5:
            fill = '0' * (5 - len(instructions))
            instructions = fill + instructions

        optcode = instructions[-1]
        params_modes = instructions[:3]
        if optcode == '99':
            return state.int_codes[0]
        if optcode == '3':
            state.set_input_at_pos(pointer)
            pointer += 2
            continue
        if optcode == '4':
            state.output(pointer, params_modes[2])
            pointer += 2
            continue
        a = int(state.param_mode_handler(params_modes[2], pointer + 1))
        b = int(state.param_mode_handler(params_modes[1], pointer + 2))
        store_loc = int(state.int_codes[pointer + 3])

        if optcode == '1':
            state.add(a, b, store_loc)
            pointer += 4
            continue
        if optcode == '2':
            state.multiply(a, b, store_loc)
            pointer += 4
            continue
        if optcode == '5':
            if a != 0:
                pointer = b
                continue
            pointer += 3
            continue
        if optcode == '6':
            if a == 0:
                pointer = b
                continue
            pointer += 3
            continue
        if optcode == '7':
            if a < b:
                state.set_value(store_loc, 1)
            else:
                state.set_value(store_loc, 0)
            pointer += 4
            continue
        if optcode == '8':
            if a == b:
                state.set_value(store_loc, 1)
            else:
                state.set_value(store_loc, 0)
            pointer += 4
            continue


def part_2():
    int_codes = get_int_codes_from_file()
    s = ProgramState(int_codes, 5)
    return run_program_part_two(s)

part_2()