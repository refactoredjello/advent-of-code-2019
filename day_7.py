from itertools import permutations


class ProgramState:
    def __init__(self, int_codes, phase, input, second_phase=False):
        self.int_codes = int_codes.copy()
        self.input = input
        self.phase = phase
        self.second_phase = second_phase
        self.halt = False

    def set_value(self, idx, val):
        self.int_codes[int(idx)] = str(val)

    def set_input_at_pos(self, idx):
        input = self.phase if not self.second_phase else self.input
        self.second_phase = True
        self.set_value(int(self.int_codes[idx + 1]), input)

    def output(self, idx, mode):
        lookup = self.param_mode_handler(mode, idx + 1)
        if lookup != '0':
            # print(f"debug idx {idx}, mode {mode}")
            return lookup

        return '0'

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
    with open('input_day_7.txt', 'r') as f:
        input = f.read()
        int_codes = [val for val in input.split(',')]

    return int_codes


def run_program(state, pointer):

    while True:
        if pointer > len(state.int_codes):
            raise IndexError(f"Pointer {pointer} out of range {len(state.int_codes)}")

        instructions = state.int_codes[pointer]
        if len(instructions) < 5:
            fill = '0' * (5 - len(instructions))
            instructions = fill + instructions

        optcode = instructions[-2:]
        params_modes = instructions[:3]

        if optcode == '99':
            return state.int_codes[0], True, 0
        if optcode == '03':
            state.set_input_at_pos(pointer)
            pointer += 2
            continue
        if optcode == '04':
            output = state.output(pointer, params_modes[2])
            if output != '0':
                return output, False, pointer + 2
            pointer += 2
            continue

        a = int(state.param_mode_handler(params_modes[2], pointer + 1))
        b = int(state.param_mode_handler(params_modes[1], pointer + 2))
        store_loc = int(state.int_codes[pointer + 3])

        if optcode == '01':
            state.add(a, b, store_loc)
            pointer += 4
            continue
        if optcode == '02':
            state.multiply(a, b, store_loc)
            pointer += 4
            continue
        if optcode == '05':
            if a != 0:
                pointer = b
                continue
            pointer += 3
            continue
        if optcode == '06':
            if a == 0:
                pointer = b
                continue
            pointer += 3
            continue
        if optcode == '07':
            if a < b:
                state.set_value(store_loc, 1)
            else:
                state.set_value(store_loc, 0)
            pointer += 4
            continue
        if optcode == '08':
            if a == b:
                state.set_value(store_loc, 1)
            else:
                state.set_value(store_loc, 0)
            pointer += 4
            continue

        raise ValueError(f"Pointer {pointer} is not a valid optcode. Value {state.int_codes[pointer]}")


# test_sequence = [4, 3, 2, 1, 0]
# test_sequence_2 = [0, 1, 2, 3, 4]
# test_sequence_3 = [1, 0, 4, 3, 2]
# test_int_codes = [str(x) for x in [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]]
# test_int_codes_2 = [str(x) for x in
#                     [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]]
# test_int_codes_3 = [str(x) for x in
#                     [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31,
#                      1, 32, 31, 31, 4, 31, 99, 0, 0, 0]]

def part_1():
    phase_settings_comb = permutations([str(x) for x in range(5)], 5)
    int_codes = get_int_codes_from_file()
    thrusts = []

    for idx, seq in enumerate(phase_settings_comb):
        input = 0
        print(f"Running seq idx: {idx}, {seq}")
        for phase in seq:
            s = ProgramState(int_codes, phase, input)
            try:
                input, _, _ = run_program(s, 0)
            except ValueError:
                break
        thrusts.append(int(input))

    print(max(*thrusts))


part_1()

# test_sequence = [9, 8, 7, 6, 5]
# test_sequence_2 = [9, 7, 8, 5, 6]
# test_int_codes = [str(x) for x in
#                   [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6,
#                    99, 0, 0, 5]]
# test_int_codes_2 = [str(x) for x in
#                     [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54,
#                      1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1,
#                      56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]]


def part_2():
    phase_settings_comb = permutations([str(x) for x in range(5, 10)], 5)
    int_codes = get_int_codes_from_file()
    thrusts = []
    start_state = {
        0: (0, False, int_codes.copy(), 0),
        1: (0, False, int_codes.copy(), 0),
        2: (0, False, int_codes.copy(), 0),
        3: (0, False, int_codes.copy(), 0),
        4: (0, False, int_codes.copy(), 0),
    }
    for idx, seq in enumerate(phase_settings_comb):
        print(f"permutation: {idx}")
        pointer_state = start_state.copy()
        input = 0
        halt = False

        while not halt:

            for pid, phase in enumerate(seq):
                # print(f"start state: {pointer_state[pid]}")
                s = ProgramState(pointer_state[pid][2], phase, input, pointer_state[pid][1])
                try:
                    output, halt, pointer = run_program(s, pointer_state[pid][0])
                    pointer_state[pid] = (pointer, True, s.int_codes, output)
                    input = output
                    print(pid, halt, pointer, output)
                except ValueError:
                    halt = True
                except IndexError:
                    halt = True

                if halt:
                    thrusts.append(int(pointer_state[4][3]))
                    break

    print(max(*thrusts))


part_2()
