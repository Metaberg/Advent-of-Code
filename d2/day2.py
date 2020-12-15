import re

input_file = open("./src/d2-input.txt", "r")
input_list = input_file.read().splitlines()


#  Solution of day 2


def solver_part1(input_list):
    valid_pw = 0
    for x in input_list:
        norm = re.split(' |: |-', x)
        occ = norm[3].count(norm[2])
        if occ >= int(norm[0]) and occ <= int(norm[1]):
            valid_pw += 1
    return valid_pw


print(solver_part1(input_list))


# Solution of day 2

def solver_part2(input_list):
    valid_pw = 0
    for x in input_list:
        norm = re.split(' |: |-', x)
        f_num = int(norm[0]) - 1
        l_num = int(norm[1]) - 1
        if norm[3][f_num] == norm[2] and not norm[3][l_num] == norm[2]:
            valid_pw += 1
        elif norm[3][l_num] == norm[2] and not norm[3][f_num] == norm[2]:
            valid_pw += 1
    return valid_pw


print(solver_part2(input_list))
