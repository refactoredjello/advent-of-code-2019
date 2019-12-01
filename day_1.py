from functools import reduce

with open('input.txt', 'r') as f:
    input = f.readlines()

##
# Part 1
##
def process_input(acc, mass):
    parsed = int(mass.rstrip("\n"))
    return acc + (parsed // 3 - 2)

initial_sum_value = reduce(process_input, input, 0)

print(initial_sum_value)

##
# Part 2
##
def recurse_fuel_mass(mass, total=0):
    fuel = mass // 3 - 2
    if fuel > 0:
        return recurse_fuel_mass(fuel, total + fuel)

    return total

def process_input_with_fuel(acc, mass):
    parsed = int(mass.rstrip("\n"))
    return acc + recurse_fuel_mass(parsed)

final_sum = reduce(process_input_with_fuel, input, 0)

print(final_sum)