from math import inf

COLUMNS = 25
ROWS = 6
LENGTH = COLUMNS * ROWS

with open("input_day_8.txt", 'r') as f:
    input = f.read().rstrip("\n")

layers = []
layer = []
print(len(input))
for idx, pixel in enumerate(input):
    layer.append(pixel)
    if (idx + 1) % (LENGTH) == 0 and idx > 0:
        layers.append(layer)
        layer = []


def counter(layer):
    count = 0
    for x in layer:
        if x == '0':
            count += 1

    return count


def find_least_zeros(layers):
    counts = {idx: counter(l) for idx, l in enumerate(layers)}
    min = inf
    min_idx = None
    for idx, count in counts.items():
        if count < min:
            min = count
            min_idx = idx

    return min_idx, min


def count_ones_twos(layer):
    ones = 0
    twos = 0
    for x in layer:
        if x == '1':
            ones += 1
        if x == '2':
            twos += 1

    return ones, twos


most_zeros_idx, max = find_least_zeros(layers)
print(most_zeros_idx, max)
ones, twos = count_ones_twos(layers[most_zeros_idx])
print(ones, twos, ones * twos)

final_layer = []
for pixel_idx in range(ROWS * COLUMNS):
    pixel = '2'
    for layer in layers:
        if layer[pixel_idx] != pixel:
            final_layer.append(layer[pixel_idx])
            break

print(final_layer)

for r_idx in range(ROWS):
    row = ["#" if final_layer[COLUMNS * r_idx + c_idx] == '1' else " " for c_idx in range(COLUMNS)]
    print("".join(row))
