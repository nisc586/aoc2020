from functools import reduce
from collections import Counter

EXAMPLE = """abc

a
b
c

ab
ac

a
a
a
a

b"""

def solve(s):
    return sum(
        len(
         reduce(
            set.intersection,
            (set(answers) for answers in group.split("\n"))))
        for group in s.split("\n\n")        
    )
       


def main():
    with open("day06/input.txt") as f:
        s = f.read()
    print(solve(s))


if __name__ == "__main__":
    assert solve(EXAMPLE) == 6
    main()
