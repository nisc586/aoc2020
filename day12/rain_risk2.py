from collections import namedtuple
import cmath
import math

Point = namedtuple("Point", ["x", "y"])

EXAMPLE = """F10
N3
F7
R90
F11"""

def parse(s):
    return [(line[0], int(line[1:])) for line in s.splitlines()]


def compute(ls):
    position = Point(0, 0)
    waypoint = Point(10, 1)

    for op, val in ls:
        if op == "F":
            position = Point(
                position.x + val * waypoint.x,
                position.y + val * waypoint.y
                )
        elif op == "N":
            waypoint = Point(
                waypoint.x,
                waypoint.y + val
                )
        elif op == "S":
            waypoint = Point(
                waypoint.x,
                waypoint.y - val
                )
        elif op == "E":
            waypoint = Point(
                waypoint.x + val,
                waypoint.y
                )
        elif op == "W":
            waypoint = Point(
                waypoint.x - val,
                waypoint.y
                )
        elif op == "L":
            # Represent waypoint in polar coordinates
            r, phi = cmath.polar(complex(waypoint.x, waypoint.y))
            phi += math.radians(val)
            z = cmath.rect(r, phi)
            waypoint = Point(round(z.real), round(z.imag))
        elif op == "R":
            r, phi = cmath.polar(complex(waypoint.x, waypoint.y))
            phi -= math.radians(val)
            z = cmath.rect(r, phi)
            waypoint = Point(round(z.real), round(z.imag))
        else:
            raise AssertionError(f"Unknown operation {op}")

    return abs(position.x) + abs(position.y)


def solve(s):
    instructions = parse(s)
    return compute(instructions)

def main():
    with open("day12/input.txt") as f:
        s = f.read()
    print(solve(s))

def test():
    assert 286 == solve(EXAMPLE)

if __name__ == "__main__":
    test()
    main()
