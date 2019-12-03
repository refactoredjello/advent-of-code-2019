from math import inf

with open('input_day_3.txt', 'r') as f:
    wire_one_vectors = f.readline().split(',')
    wire_two_vectors = f.readline().split(',')


## Test Cases ##
# wire_one_vectors = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
# wire_two_vectors = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')


def move_y(point, displacement, direction):
    sign = -1 if direction == 'D' else 1
    new_points = []

    for y in range(sign, displacement * sign + sign, sign):
        new_points.append((point[0], point[1] + y))

    return new_points


def move_x(point, displacement, direction):
    sign = -1 if direction == 'L' else 1
    new_points = []

    for x in range(sign, displacement * sign + sign, sign):
        new_points.append((point[0] + x, point[1]))

    return new_points


def move(point, direction, displacement):
    if direction in ['U', 'D']:
        return move_y(point, displacement, direction)
    else:
        return move_x(point, displacement, direction)


def parse_vector(v):
    direction = v[0]
    displacement = int(v[1:])

    return direction, displacement


def run_vectors(vectors):
    points = [(0, 0)]
    for vector in vectors:
        direction, displacement = parse_vector(vector)
        new_points = move(points[-1], direction, displacement)
        points.extend(new_points)

    return points


wire_one_points = run_vectors(wire_one_vectors)
wire_two_points = run_vectors(wire_two_vectors)


def find_intersection():
    return set(wire_one_points) & set(wire_two_points)


intersections = find_intersection()


def manhattan_distance(intersections):
    distances = []
    for point in intersections:
        if point == (0, 0):
            continue
        distances.append(abs(0 - point[0]) + abs(0 - point[1]))

    return distances


print("Intersections")
print(intersections)
print("Finding min distance")
print(min(*manhattan_distance(intersections)))


def count_steps(wire_points):
    intersection_steps = {}
    for point in intersections:
        if point in wire_points and point != (0, 0):
            intersection_steps[str(point)] = wire_points.index(point)

    return intersection_steps


def combine_steps():
    wire_one_intersection_steps = count_steps(wire_one_points)
    wire_two_intersection_steps = count_steps(wire_two_points)

    min = inf
    for point, steps in wire_one_intersection_steps.items():
        sum_steps = steps + wire_two_intersection_steps[point]
        min = min if min < sum_steps else sum_steps

    return min


print("Finding min combined steps")
print(combine_steps())
