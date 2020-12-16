def ticket_translation():
    with open('day16.txt') as ticket_file:
        lines = [line.strip() for line in ticket_file.readlines()]

    rules = []
    for i in range(20):
        line = lines[i].split()
        if len(line) == 5:
            values1 = line[2].split('-')
            values2 = line[4].split('-')
        else:
            values1 = line[1].split('-')
            values2 = line[3].split('-')
        rules.append([])
        rules[i].extend(range(int(values1[0]), int(values1[1])+1))
        rules[i].extend(range(int(values2[0]), int(values2[1])+1))
    
    error_rate = 0
    valids = []
    for i, ticket in enumerate(lines[25:]):
        valid = True
        values = list(map(int, ticket.split(',')))
        for value in values:
            z = any([value in rule for rule in rules])
            if not z:
                valid = False
                error_rate += value
        if valid:
            valids.append(list(map(int, lines[i+25].split(','))))
    
    print(error_rate)

    """
    PART 2: didn't write code to spit out the result and had to iteratively
    change things and on top of that, guess which value represents the last
    (6th) field!
    """
    number_of_values = len(lines[25].split(','))
    rules.pop(0)
    rules.pop(1)
    rules.pop(1)
    rules.pop(1)
    rules.pop(0)
    for i in range(number_of_values):
        vals = [values[i] for values in valids]
        satisfies = [False] * 1
        for rule_number, rule in enumerate(rules[:1]):
            if all([values[i] in rule for values in valids]):
                satisfies[rule_number] = True
        print(i, satisfies)
        if sum(satisfies) == 1:
            print(i, satisfies.index(True))

    """
    PART 2 result is 910339449193, the corresponding values and fields are:
    field: value_index - index starts at 0
    departure location: 2
    departure station: 5
    departure platform: 17
    departure track: 19
    departure date: 10
    departure time: 15
    """


if __name__ == '__main__':
    ticket_translation()