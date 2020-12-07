def password_philosophy():
    with open('Day2.txt') as passwords_file:
        lines = [line.strip() for line in passwords_file.readlines()]
    number_of_valid_passwords = 0
    part_2 = 0
    for line in lines:
        split = line.split(' ')
        first_word = split[0].split('-')
        occurences = (int(first_word[0]), int(first_word[1]))
        letter = split[1][0]
        password = split[2]
        count = password.count(letter)
        if count <= occurences[1] and count >= occurences[0]:
            number_of_valid_passwords += 1
        if (password[occurences[0]-1] == letter and \
            password[occurences[1]-1] != letter) or \
            (password[occurences[0]-1] != letter and
            password[occurences[1]-1] == letter):
            part_2 += 1
    print('Number of valid passwords is:', number_of_valid_passwords)
    print('Number of valid passwords for part 2 is:', part_2)

if __name__ == '__main__':
    password_philosophy()
