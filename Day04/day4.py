def passport_processing():
    with open('day4.txt') as batch_file:
        lines = [line.strip() for line in batch_file.readlines()]
    
    current_passport = {}
    valid_passports = 0
    valid_valid_passports = 0
    fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for line in lines:
        if line == '':
            if fields.issubset(set(current_passport.keys())):
                valid_passports += 1
                if quick_data_validation(current_passport):
                    valid_valid_passports += 1
            current_passport = {}
        else:
            for pair in line.split():
                key, value = pair.split(':')
                current_passport[key] = value
    if fields.issubset(set(current_passport.keys())):
        valid_passports += 1
    print("Number of valid passwords:", valid_passports)
    print("Number of valid valid passwords:", valid_valid_passports)

def quick_data_validation(passport: dict) -> bool:
    byr = int(passport['byr'])
    if byr < 1920 or byr > 2002:
        return False
    iyr = int(passport['iyr'])
    if iyr < 2010 or iyr > 2020:
        return False
    eyr = int(passport['eyr'])
    if eyr < 2020 or eyr > 2030:
        return False
    hgt = int(passport['hgt'][:-2])
    if 'cm' in passport['hgt']:
        if hgt < 150 or hgt > 193:
            return False
    elif 'in' in passport['hgt']:
        if hgt < 59 or hgt > 76:
            return False
    if len(passport['hcl']) != 7 and '#' not in passport['hcl']:
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if len(passport['pid']) != 9:
        return False
    return True

if __name__ == '__main__':
    passport_processing()