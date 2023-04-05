from collections import namedtuple
import math


EXAMPLE = """F10
N3
F7
R90
F11"""

Position = namedtuple("Position", ["x", "y"])


def parse(s):
    return [(line[0], int(line[1:])) for line in s.splitlines()]


def compute(ls):
    pos = Position(0, 0)
    direction = 0

    for op, val in ls:
        if op == "F":
            dx = round(math.cos(math.radians(direction)))
            dy = round(math.sin(math.radians(direction)))
            pos = Position(pos.x + val*dx, pos.y + val*dy)
        elif op == "N":
            pos = Position(pos.x, pos.y + val)
        elif op == "S":
            pos = Position(pos.x, pos.y - val)
        elif op == "E":
            pos = Position(pos.x + val, pos.y)
        elif op == "W":
            pos = Position(pos.x - val, pos.y)
        elif op == "L":
            direction += val
        elif op == "R":
            direction -= val
        else:
            raise AssertionError(f"Unknown operation {op}")

    return abs(pos.x) + abs(pos.y)


def solve(s):
    instructions = parse(s)
    return compute(instructions)

def main():
    with open("day12/input.txt") as f:
        s = f.read()
    print(solve(s))


def test():
    assert 25 == solve(EXAMPLE)

if __name__ == "__main__":
    test()
    main()
