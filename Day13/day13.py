import math

def shuttle_search():
    with open('day13.txt') as notes:
        lines = [line.strip() for line in notes.readlines()]
    earliest_timestamp = int(lines[0])
    times = {}
    for ID in lines[1].split(','):
        if ID != 'x':
            ID = int(ID)
            koef = int(earliest_timestamp/ID)
            time = koef*ID
            if koef*ID != earliest_timestamp:
                times[ID] = time + ID
            else:
                print('Part 1 result is:', 0)
                return

    min_ID = min(times, key=times.get)
    print('Part 1 result is:', min_ID*(times[min_ID]-earliest_timestamp))

    # least common multiple of lines that need to start at the same time
    num = 152016397
    while num < 100000000000000:
        num += 152016397
    current_multiple = num

    line = lines[1].split(',')

    # find multiple that corresponds with other bus lines
    while True:
        target = current_multiple - 19
        if target % 37 == 24 and target % 23 == 19 \
            and target % 797 == 747 and target % 29 == 8:
            print('Part 2 result is:', current_multiple - 19)
            break
        current_multiple += 152016397


if __name__ == '__main__':
    shuttle_search()