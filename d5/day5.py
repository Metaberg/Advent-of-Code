input_file = open("./src/d5-input.txt", "r")
code = [l.rstrip('\n') for l in input_file]
input_file.close()


def solver(code):
    '''
    Replaces the given string in binary.
    Returns list with all available seats
    '''
    av_seat = []
    num_raw = 0
    for l in code:
        l = l.replace('F', '0')
        l = l.replace('B', '1')
        l = l.replace('L', '0')
        l = l.replace('R', '1')
        num_raw = int(l, 2)  # binary 0b or 0B
        av_seat.append(num_raw)

    return av_seat


print(max(solver(code)))

seats = (solver(code))
all_seats = range(min(seats), max(seats))


for seat in all_seats:
    if seat not in seats and seat - 1 in seats and seat + 1 in seats:
        print(seat)
