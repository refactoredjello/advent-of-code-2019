from collections import defaultdict

lower_bound = 136760
upper_bound = 595730

all_possible_values = [str(n) for n in range(lower_bound + 1, upper_bound)]


def check_ascend(values):
    for i, val in enumerate(reversed(values)):
        for test_val in values[:5 - i]:
            if val < test_val:
                return False

    return True


def check_repeating(values):
    for i, val in enumerate(values):
        if i > 4:
            return False

        if val == values[i + 1]:
            return True


def filter_rules(values):
    if not check_ascend(values):
        return False

    if not check_repeating(values):
        return False

    return True


filtered_values = [v for v in all_possible_values if filter_rules(v)]
print(len(filtered_values))


def check_repeating_doubles(values):
    test = None
    runs = defaultdict(int)
    queue = list(values[-1::-1])

    while queue:
        last = queue.pop()
        if last == test:
            runs[last] += 1

        test = last
    if not runs:
        return False

    return runs and any(val == 1 for val in runs.values())


# Got lazy
def filter_rules_part_two(values):
    if not check_ascend(values):
        return False

    if not check_repeating_doubles(values):
        return False

    return True


filtered_values = [v for v in all_possible_values if filter_rules_part_two(v)]
print(len(filtered_values))
