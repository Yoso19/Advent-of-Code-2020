def toboggan_trajectory():
    with open('Day3.txt') as tree_map:
        lines = [line.strip() for line in tree_map.readlines()]
        result = 1
        for x, y in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
            result *= go_down_slope(lines, x, y)
        print(result)

def go_down_slope(lines, x, y):
    current_x = 0
    trees = 0
    width = len(lines[0])
    for current_y in range(0, len(lines), y):
        if lines[current_y][current_x] == '#':
            trees += 1
        current_x = (current_x + x) % width
    print(str(x)+','+str(y)+':', trees)
    return trees

    
if __name__ == '__main__':
    toboggan_trajectory()