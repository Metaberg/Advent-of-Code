input_file = open("./src/d6-input.txt", "r")
code = input_file.read() .split('\n\n')
input_file.close()


def solver(code):
    count = 0
    questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for data in code:
        group = data.split('\n')
        used = []
        for pers in group:
            for i in questions:
                if i in pers and i not in used:
                    used.append(i)
                    count += 1
    return count


print(solver(code))
