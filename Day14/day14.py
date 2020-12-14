from copy import deepcopy

def docking_data():
    with open('day14.txt') as program_file:
        lines = [line.strip() for line in program_file.readlines()]
    memory = {}

    for line in lines:
        if line.startswith('mask'):
            mask_ = line.split()[-1]
        else:
            split = line.split()
            location = int(split[0][4:-1])
            value = str(format(int(split[2]), '036b'))
            memory[location] = mask(mask_, value)

    result = 0
    for key, value in memory.items():
        result += int(value, 2)
    print('Sum of all values left in memory is:', result)

    memory = {}
    for line in lines:
        if line.startswith('mask'):
            mask_ = line.split()[-1]
        else:
            split = line.split()
            location = str(format(int(''.join(split[0][4:-1])), '036b'))
            value = int(split[2])
            for loc in mask2(mask_, location):
                memory[int(''.join(loc),2)] = value

    result = 0
    for key, value in memory.items():
        result += value
    print('Sum of all values left in memory is:', result)

def mask(mask, value):
    mask = list(mask)
    value = list(value)
    for i in range(len(mask)):
        if mask[i] == 'X':
            continue
        if mask[i] == '0':
            value[i] = '0'
        else:
            value[i] = '1'
    return ''.join(value)

def mask2(mask, location):
    mask = list(mask)
    location = list(location)
    floating = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            floating.append(i)
        if mask[i] == '0':
            continue
        else:
            location[i] = '1'
    result = []
    for flo in floating:
        if not result:
            res1 = deepcopy(location)
            res1[flo] = '0'
            result.append(res1)
            res2 = deepcopy(location)
            res2[flo] = '1'
            result.append(res2)
        else:
            temp = deepcopy(result)
            res = []
            for loca in temp:
                loca[flo] = '0'
                res.append(deepcopy(loca))
                loca[flo] = '1'
                res.append(deepcopy(loca))
            result = res
    return result


if __name__ == '__main__':
    docking_data()