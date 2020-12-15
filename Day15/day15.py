def rambunctious_recitation():
    with open('day15.txt') as numbers_file:
        line = numbers_file.readlines()[0].split(',')
        starting_numbers = [int(number) for number in line]
    
    spoken = {}
    for i, number in enumerate(starting_numbers): 
        spoken[number] = (i+1, 0)
    spoken[0] = (7, 1)
    turn = 7
    last = 0
    while True:
        # for part 1 change number to 2020
        if turn == 30000000:
            print(turn, last)
            break
        if spoken[last][1] == 0:
            last = 0
        else:
            last = spoken[last][0] - spoken[last][1]
        turn += 1
        if spoken.get(last, 0) == 0:
            spoken[last] = (turn, 0)
        else:
            spoken[last] = (turn, spoken[last][0])


if __name__ == '__main__':
    rambunctious_recitation()