input_file = open("./src/d6-input.txt", "r")
code = input_file.read() .split('\n\n')
input_file.close()


def solver(code):
    count = 0
    questions = list(map(chr, range(97, 123)))  # Fill list with alphabet
    for data in code:
        group = data.split('\n')
        used = []
        for p in group:
            for i in questions:
                # Part 1 in comments
                # if i in p and i not in used:
                #     used.append(i)
                #     count += 1
                if i in p:
                    used.append(i)
        for t in used:
            if used.count(t) == len(group):
                used = list(filter(lambda x: x != t, used))
                count += 1
    return count


print(solver(code))
