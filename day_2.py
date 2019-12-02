class ProgramState:
    def __init__(self, int_codes):
        self.int_codes = int_codes

    def get_handler(self, optcode):
        optcode_handlers = {
            1: self.add,
            2: self.multiply,
        }

        return optcode_handlers[optcode]

    def get_value(self, idx):
        val_loc = self.int_codes[idx]
        return self.int_codes[val_loc]

    def set_value(self, idx, val):
        self.int_codes[idx] = val

    def add(self, a, b, set_idx):
        val = a + b
        self.set_value(set_idx, val)

    def multiply(self, a, b, set_idx):
        val = a * b
        self.set_value(set_idx, val)

    # Set state to "1202 program alarm"
    def set_inputs(self, noun, verb):
        self.int_codes[1] = noun
        self.int_codes[2] = verb


def set_int_codes_from_file():
    with open('input_day_2.txt', 'r') as f:
        input = f.read().rstrip('\n')
        int_codes = [int(val) for val in input.split(',')]

    return int_codes


def run_program(state):
    for idx in range(0, len(state.int_codes), 4):
        optcode = state.int_codes[idx]

        if optcode == 99:
            return state.int_codes[0]

        handler = state.get_handler(optcode)

        a = state.get_value(idx + 1)
        b = state.get_value(idx + 2)
        store_loc = state.int_codes[idx + 3]
        handler(a, b, store_loc)
##
# Part 1
##
def part_1():
    int_codes = set_int_codes_from_file()
    s = ProgramState(int_codes)
    s.set_inputs(12, 2)
    return run_program(s)

print(f"Part 1 answer {part_1()}")

##
# Part 2
##
def part_2():
    target_value = 19690720

    for noun in range(0, 100):

        for verb in range(0, 100):

            int_codes = set_int_codes_from_file()
            s = ProgramState(int_codes)
            s.set_inputs(noun, verb)

            if run_program(s) == target_value:
                return noun, verb


noun, verb = part_2()
print(f"Part 2 answer: {100 * noun + verb}")
