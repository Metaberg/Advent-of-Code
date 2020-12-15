import re

input_file = open("./src/d4-input.txt", "r")
input_list = input_file.read().split('\n\n')
input_file.close()


def solver(passports):
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = 0
    for p in passports:
        norm = re.split(' |:|\n', p)
        # print(norm)

        no_req = 0
        is_valid = False
        for req in req:
            if req in norm:
                no_req += 1
                idx = norm.index(req) + 1
                value = norm[idx]

                if value not in req:
                    if req == 'byr':
                        is_valid = 1920 <= int(value) <= 2002
                    elif req == 'iyr':
                        is_valid = 2010 <= int(value) <= 2020
                    elif req == 'eyr':
                        is_valid = 2020 <= int(value) <= 2030
                    elif req == 'hgt':
                        if 'cm' in value:
                            is_valid = 150 <= int(value[:-2]) <= 193
                        elif 'in' in value:
                            is_valid = 59 <= int(value[:-2]) <= 76
                    elif req == 'hcl':
                        str_val = str(value)
                        # print(str_val)
                        is_valid = bool(re.match(
                            r'#[0-9a-f]{6}', str_val))
                    elif req == 'ecl':
                        is_valid = value in 'amb blu brn gry grn hzl oth'.split()
                    elif req == 'pid':
                        str_val = str(value)
                        is_valid = bool(re.match(
                            r'[0-9]{9}', str_val))
                    elif req == 'cid':
                        is_valid = True

        if no_req == 7 and is_valid:
            valid += 1
    return valid


print(solver(input_list))
