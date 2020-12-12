
input_file = open("./src/d1-input.txt", "r")
input_list = input_file.read().splitlines()

# Solution of Part 1


def solver_part1(input_list):
    for x in input_list:
        target = 2020 - int(x)
        if input_list.count(str(target)):
            return int(x) * target


print(solver_part1(input_list))

# Solution of Part 2


def solver_part2(input_list):
    for x in input_list:
        for y in input_list:
            target = 2020 - int(x) - int(y)
            if input_list.count(str(target)):
                return int(x) * int(y) * target


print(solver_part2(input_list))
