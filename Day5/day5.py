def binary_boarding():
    with open('day5.txt') as boarding_passes:
        passes = [line.strip() for line in boarding_passes]
    mappings = [('F', '0'), ('B', '1'), ('R','1'), ('L','0')]
    for mapping in mappings:
        passes = list(map(lambda p: p.replace(mapping[0], mapping[1]), passes))
    rows = list(map(lambda p: int(p[:7], 2), passes))
    columns = list(map(lambda p: int(p[-3:], 2), passes))
    seat_IDs = [row*8 + column for row, column in zip(rows,columns)]
    print('Highest seat ID is:', max(seat_IDs))

    for ID in range(21, 997):
        if ID not in seat_IDs:
            print('ID of my seat is:', ID)

if __name__ == '__main__':
    binary_boarding()