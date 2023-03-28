def seat_id(s):
    for c, i in zip("FBLR", "0101"):
        s = s.replace(c, i)
    return int(s, base=2)

def solve():
    with open("day05/input.txt") as f:
        result = max(
            seat_id(s)
            for s in f.readlines()
        )
    print(result)

if __name__ == "__main__":

    assert seat_id("BFFFBBFRRR") == 567
    assert seat_id("FFFBBBFRRR") == 119
    assert seat_id("BBFFBBFRLL") == 820

    solve()