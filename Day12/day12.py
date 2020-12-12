def rain_risk():
    with open('day12.txt') as instruction_file:
        instructions = [list(line.strip()) for line \
            in instruction_file.readlines()]
    part1(instructions)
    part2(instructions)

def part1(instructions):
    facing = 'E'
    sides = ['W', 'N', 'E', 'S']
    x = 0
    y = 0
    for instruction in instructions:
        action, value = instruction[0], int(''.join(instruction[1:]))
        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'L':
            times = int(value/90)
            index = sides.index(facing)
            facing = sides[(index-times)%4]
        elif action == 'R':
            times = int(value/90)
            index = sides.index(facing)
            facing = sides[(index+times)%4]
        else:
            if facing == 'E':
                x += value
            elif facing == 'N':
                y += value
            elif facing is 'W':
                x -= value
            else:
                y -= value
    
    print('Manhattan distance is:', abs(x) + abs(y))

def part2(instructions):
    waypoint_x = 10
    waypoint_y = 1
    sides = ['W', 'N', 'E', 'S']
    x = 0
    y = 0
    for instruction in instructions:
        action, value = instruction[0], int(''.join(instruction[1:]))
        if action == 'N':
            waypoint_y += value
        elif action == 'S':
            waypoint_y -= value
        elif action == 'E':
            waypoint_x += value
        elif action == 'W':
            waypoint_x -= value
        elif action == 'L':
            times = int(value/90)
            if times == 1:
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
            if times == 2:
                waypoint_x, waypoint_y = -waypoint_x, -waypoint_y
            if times == 3:
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif action == 'R':
            times = int(value/90)
            if times == 1:
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
            if times == 2:
                waypoint_x, waypoint_y = -waypoint_x, -waypoint_y
            if times == 3:
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        else:
            x += value * waypoint_x
            y += value * waypoint_y
    
    print('Manhattan distance is:', abs(x) + abs(y))


if __name__ == '__main__':
    rain_risk()