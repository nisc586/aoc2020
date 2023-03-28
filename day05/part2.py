def seat_id(s):
    for c, i in zip("FBLR", "0101"):
        s = s.replace(c, i)
    return int(s, base=2)

def solve():
    with open("day05/input.txt") as f:
        # Mark all seats as free
        seats = [True] * 2**10
        for s in f.readlines():
            seats[seat_id(s)] = False
    
    for i in range(100):
        # Mark seats at the front and back as not free
        seats[i] = False
        seats[-i] = False
    
    assert seats.count(True) == 1
    print(seats.index(True))

if __name__ == "__main__":

    assert seat_id("BFFFBBFRRR") == 567
    assert seat_id("FFFBBBFRRR") == 119
    assert seat_id("BBFFBBFRLL") == 820

    solve()