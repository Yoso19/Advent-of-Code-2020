import itertools

def report_repair():
    with open('day1.txt') as report:
        expense = [int(x) for x in report.readlines()]
        for first, second in itertools.product(expense, expense):
            if first + second == 2020:
                print('Product of two entries that sum to 2020 is:', \
                    first * second)
                break
        for first, second, third in itertools.product( \
            expense, expense, expense):
            if first + second + third == 2020:
                print('Product of three entries that sum to 2020 is:', \
                    first * second * third)
                return


if __name__ == '__main__':
    report_repair()