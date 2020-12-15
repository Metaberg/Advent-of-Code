input_file = open("./src/d5-input.txt", "r")
code = [l.rstrip('\n') for l in input_file]
input_file.close()


def solver(code_to_solve):
    av_seat = []
    for c in code_to_solve:
        c = c.replace('F', '0')
        c = c.replace('B', '1')
        c = c.replace('L', '0')
        c = c.replace('R', '1')
        num_raw = int(c, 2)  # binary 0b or 0B
        av_seat.append(num_raw)

    return av_seat


print(max(solver(code)))

seats = (solver(code))
all_seats = range(min(seats), max(seats))

for seat in all_seats:
    if seat not in seats and seat - 1 in seats and seat + 1 in seats:
        print(seat)
