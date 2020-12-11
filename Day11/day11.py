from itertools import product
from copy import deepcopy

def seating_system():
    with open('day11.txt') as layout_file:
        seat_layout = [list(line.strip()) for line in layout_file.readlines()]
    part1(seat_layout)
    part2(seat_layout)

def part1(seat_layout):
    situation_changed = True
    length = len(seat_layout[0])
    height = len(seat_layout)

    while situation_changed:
        new_seat_layout = deepcopy(seat_layout)
        situation_changed = False
        for y in range(height):
            for x in range(length):
                seat = seat_layout[y][x]
                if seat == '.':
                    continue
                elif seat == 'L':
                    if check(seat_layout, x, y) == 0:
                        situation_changed = True
                        new_seat_layout[y][x] = '#'
                else:
                    if check(seat_layout, x, y) >= 4:
                        situation_changed = True
                        new_seat_layout[y][x] = 'L'
        seat_layout = deepcopy(new_seat_layout)

    occupied = 0
    for row in seat_layout:
        occupied += row.count('#')

    print('Number of occupied seats is:', occupied)

def check(layout, x, y):
    occupied = 0
    length = len(layout[0])
    height = len(layout)
    for x_diff, y_diff in product(range(-1,2), range(-1,2)): 
        if x_diff != 0 or y_diff != 0:
            new_x = x + x_diff
            new_y = y + y_diff
            if new_y >= 0 and new_y < height and new_x >= 0 and new_x < length:
                if layout[new_y][new_x] == '#':
                    occupied += 1
    return occupied

def part2(seat_layout):
    situation_changed = True
    length = len(seat_layout[0])
    height = len(seat_layout)
    iteration = 0
    directions = list(product(range(-1,2), range(-1,2)))
    directions.remove((0,0))

    while situation_changed:
        new_seat_layout = deepcopy(seat_layout)
        situation_changed = False
        for y in range(height):
            for x in range(length):
                seat = seat_layout[y][x]
                if seat == '.':
                    continue
                elif seat == 'L':
                    if check2(seat_layout, x, y, directions) == 0:
                        situation_changed = True
                        new_seat_layout[y][x] = '#'
                else:
                    if check2(seat_layout, x, y, directions) >= 5:
                        situation_changed = True
                        new_seat_layout[y][x] = 'L'
        seat_layout = deepcopy(new_seat_layout)
        iteration += 1

    occupied = 0
    for row in seat_layout:
        occupied += row.count('#')

    print('Number of occupied seats is:', occupied)

def check2(layout, x, y, directions):
    occupied = 0
    length = len(layout[0])
    height = len(layout)
    for direction in directions:
        new_x = x
        new_y = y
        while not new_y < 0 or new_y == height \
            or not new_x < 0 or new_x == length:
            new_x += direction[0]
            new_y += direction[1]
            if new_y < 0 or new_y >= height or new_x < 0 or new_x >= length:
                break
            if layout[new_y][new_x] == 'L':
                break    
            if layout[new_y][new_x] == '#':
                occupied += 1
                break
    return occupied


if __name__ == '__main__':
    seating_system()