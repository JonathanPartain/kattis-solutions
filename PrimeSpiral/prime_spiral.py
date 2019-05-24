import fileinput
from itertools import cycle
from collections import deque
# Kattis Prime Spiral
# https://open.kattis.com/problems/spiral

def move_right(x, y):
    return x+1, y


def move_up(x, y):
    return x, y+1


def move_left(x, y):
    return x-1, y


def move_down(x, y):
    return x, y-1


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    for number in range(3, int(n**0.5)+1, 2):  # only odd numbers
        if n % number == 0:
            return False
    return True


def generate(end):
    dict = {}
    reverse = {}

    # cycle moves
    times_to_move = 1
    cycle_moves = cycle(moves)

    number = 1
    position = (0, 0)
    dict[number] = position
    reverse[position] = number

    while True:
        for a in range(2):
            move = next(cycle_moves)
            for num in range(times_to_move):
                if times_to_move >= end:
                    return dict, reverse
                position = move(*position)
                number += 1

                dict[number] = position
                reverse[position] = number

        times_to_move += 1


def solve(start_pos, end_pos, case):
    global items_left
    global items_next

    positions = [tuple((end_pos[0]+1, end_pos[1])),
                 tuple((end_pos[0]-1, end_pos[1])),
                 tuple((end_pos[0], end_pos[1]+1)),
                 tuple((end_pos[0], end_pos[1]-1))]

    possible = False
    for pos in positions:
        if not is_prime(reverse.get(pos, False)):
            possible = True

    if is_prime(reverse.get(start_pos, False)) or is_prime(reverse.get(end_pos, False)):
        possible = False

    if not possible:
        print("Case %d: impossible" % case)
        return

    counter = 0

    x_queue.append(x_pos)
    y_queue.append(y_pos)

    visited.add((x_pos, y_pos))

    while len(x_queue) > 0:
        x = x_queue.popleft()
        y = y_queue.popleft()

        if (x, y) == end_position:
            print("Case %d: %d" % (case, counter))
            return

        for x_new, y_new in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            check = is_prime(reverse.get((x_new, y_new), False))
            if (x_new, y_new) not in visited and check is False:
                x_queue.append(x_new)
                y_queue.append(y_new)
                items_next += 1
                visited.add((x_new, y_new))

        items_left -= 1

        if items_left == 0:
            items_left = items_next
            items_next = 0
            counter += 1

    print("Case %d: impossible" % case)
    return


file = fileinput.input()
case = 1
# order of moves
moves = [move_right, move_up, move_left, move_down]
dictionary, reverse = generate(101)  # generate list with higher threshold than the ending

for line in fileinput.input():
    input_string = line.strip().split()

    items_left = 1
    items_next = 0

    start = int(input_string[0])
    end = int(input_string[1])

    start_position = dictionary[start]  # value
    end_position = dictionary.get(end)  # x/y tuple
    current_position = start_position  # x/y tuple

    x_queue = deque([])
    y_queue = deque([])
    # set of visited places
    visited = set()

    x_pos = current_position[0]
    y_pos = current_position[1]

    # direction vectors
    d_x = [-1, +1, 0, 0]
    d_y = [0, 0, +1, -1]

    reached_end = False

    solve(start_position, end_position, case)
    case += 1

