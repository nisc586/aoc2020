from collections import deque

EXAMPLE = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def parse(s):
    return [int(line) for line in s.splitlines()]


def is_valid(number, preamble):
    seen = set()
    for x in preamble:
        if number-x in seen:
            return True
        else:
            seen.add(x)
    return False


def solve(s, preamble_length=5):
    data = parse(s)
    preamble = deque(data[:preamble_length], maxlen=preamble_length)
    others = data[preamble_length:]

    while others:
        x = others.pop(0)
        if is_valid(x, preamble):
            preamble.append(x)
        else:
            return x
    else:
        raise AssertionError("unreachable")
    

def main():
    with open("day09/input.txt") as f:
        s = f.read()
    print(solve(s, preamble_length=25))


if __name__ == "__main__":
    assert solve(EXAMPLE, preamble_length=5) == 127
    main()