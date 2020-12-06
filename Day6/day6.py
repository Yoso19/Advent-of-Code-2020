def custom_customs():
    with open('day6.txt') as answer_file:
        lines = [line.strip() for line in answer_file.readlines()]
    groups = []
    yes = set()
    group_part2 = []
    groups_part2 = []
    for line in lines:
        if line == '':
            groups.append(yes)
            yes = set()
            groups_part2.append(group_part2)
            group_part2 = []
        else:
            yes.update(list(line))
            group_part2.append(set(list(line)))
    groups.append(yes)
    groups_part2.append(group_part2)
    intersections = [len(set.intersection(*group)) for group in groups_part2]
    print('Sum of counts is:', sum(map(len, groups)))
    print('Sum of those counts is:', sum(intersections))
        

if __name__ == '__main__':
    custom_customs()