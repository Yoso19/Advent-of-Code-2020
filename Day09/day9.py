def encoding_error():
    with open('day9.txt') as encrypted_data:
        data = [int(line.strip()) for line in encrypted_data.readlines()]

    PREAMBLE = 25

    for i, number in enumerate(data[PREAMBLE:]):
        number_property = False
        i += PREAMBLE
        preamble_ = data[i-PREAMBLE:i]
        for j, preamble_number in enumerate(preamble_[:-1]):
            temp_preamble = preamble_.copy()
            del temp_preamble[j]
            if number - preamble_number in temp_preamble:
                number_property = True
                break
        if not number_property:
            result = number
            print('First number that does not have the property is:', number)
            break

    index = data.index(result)
    data = data[:index]
    length = len(data)
    for i in range(length):
        target = result
        nums = []
        while target > 0:
            nums.append(data[length-i-1])
            target -= data[length-i-1]
            i += 1
        if target == 0:
            break
    nums.sort()
    print('Encryption weakness is:', nums[0] + nums[-1])


if __name__ == '__main__':
    encoding_error()