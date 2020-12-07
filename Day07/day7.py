import re

def handy_haversacks():
    with open('day7.txt') as rules_file:
        rules = [line.strip() for line in rules_file.readlines()]
    bags = {}
    for rule in rules:
        split = rule.split()
        color = split[0] + ' ' + split[1]
        matches = re.findall('([1-9]+) ([a-z]+) ([a-z]+) bag', rule)
        for i, match in enumerate(matches):
            matches[i] = (match[0], match[1] + ' ' + match[2])
        bags[color] = matches
    can_contain_gold = 0
    for color in bags.keys():
        if go_in_bag(color, bags):
            can_contain_gold += 1

    required_bags_in_gold = 0
    for bag in bags['shiny gold']:
        required_bags_in_gold += count_the_bags(bag[1], bags) * int(bag[0])

    print('Bags that can eventually contain at least one shiny gold bag:', \
        can_contain_gold)
    print('Number of individual bags inside single shiny gold bag is:', \
        required_bags_in_gold)

def count_the_bags(color, bags):
    count = 1
    if not bags[color]:
        return count
    for bag in bags[color]:
        count += count_the_bags(bag[1], bags) * int(bag[0])
    return count

def go_in_bag(color, bags):
    if not bags[color]:
        return False
    if 'shiny gold' in [x[1] for x in bags[color]]:
        return True
    else:
        gold = []
        for bag in bags[color]:
            gold.append(go_in_bag(bag[1], bags))
        return any(gold)


if __name__ == '__main__':
    handy_haversacks()