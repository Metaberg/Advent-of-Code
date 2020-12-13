from itertools import count, islice

input_file = open("./src/d3-input.txt", "r")
forest = [l.rstrip('\n') for l in input_file]
input_file.close()


def solver(r, d):
    '''
    Returns the number of trees of the given Map (forest)
    Uses out of global the iterable -> Map (forest)
    r = right
    d = down
    '''
    rows = islice(forest, None, None, d)
    cols = count(step=r)
    return sum(row[col % len(row)] == '#' for (row, col) in zip(rows, cols))


print(
    solver(1, 1)
    * solver(3, 1)  # Part 1 slope
    * solver(5, 1)
    * solver(7, 1)
    * solver(1, 2)
)
