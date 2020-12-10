from itertools import groupby

def adapter_array():
    with open('day10.txt') as joltage_file:
        output_joltages = [int(line.strip()) for line in \
            joltage_file.readlines()]
    output_joltages.sort()
    built_in_adapter = output_joltages[-1] + 3

    current_joltage = 0
    number_of_differences = [0, 0, 0]
    output_joltages.insert(0, 0)
    output_joltages.append(built_in_adapter)
    differences = []
    for i in range(len(output_joltages)-1):
        difference = output_joltages[i+1] - output_joltages[i]
        differences.append(difference)
        number_of_differences[difference-1] += 1

    print('Number of 1-jolt differences multiplied by the number of 3-jolt ' +
        'differences is:', number_of_differences[0] * \
            number_of_differences[2])

    lengths=[]
    for k, g in groupby(differences):
        if k == 1:
            lengths.append(len(list(g)))

    result=1
    for length in lengths:
        if length == 4:
            result *= 7
        if length == 3:
            result *= 4
        if length == 2:
            result *= 2

    print('Total number of distinct ways is:', result)


if __name__ == '__main__':
    adapter_array()
