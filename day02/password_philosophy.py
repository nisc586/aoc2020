import re
from collections import namedtuple, Counter

Rule = namedtuple("Rule", ["a", "b", "letter", "password"])

EXAMPLE = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

def parse(s):
    pattern = r"^(\d+)-(\d+) (\w): (\w+)$"
    return [
        Rule(*re.match(pattern, line).groups())
        for line in s.splitlines()
    ]


def solve1(s):
    total = 0
    for rule in parse(s):
        c = Counter(rule.password)
        if int(rule.a) <= c[rule.letter] <= int(rule.b):
            total += 1
    return total


def solve2(s):
    return sum(
        # != is the same as xor, the indexes in the rules start at 1
        (rule.password[int(rule.a)-1] == rule.letter) != (rule.password[int(rule.b)-1] == rule.letter)
        for rule in parse(s)
    )
        

def main():
    with open("day02/input.txt") as f:
        s = f.read()
    print("Part 1:", solve1(s))
    print("Part 2:", solve2(s))


if __name__ == "__main__":
    assert solve1(EXAMPLE) == 2, f"example was not solved correctly. expected: 2 got: {solve1(EXAMPLE)}"
    assert solve2(EXAMPLE) == 1, f"example was not solved correctly. expected: 2 got: {solve2(EXAMPLE)}"
    main()