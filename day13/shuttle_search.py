import re

EXAMPLE = """939
7,13,x,x,59,x,31,19"""

def parse(s):
    lines = s.splitlines()
    now = int(lines[0])
    busses = [int(id) for id in re.findall(r"\d+", lines[1])]
    return now, busses

def compute(now, busses):
    wait_time = 99999
    best_bus = -1
    for bus in busses:
        departs_in = (bus - now % bus) % bus
        if departs_in < wait_time:
            wait_time = departs_in
            best_bus = bus
    return best_bus * wait_time


def test():
    assert 295 == compute(*parse(EXAMPLE))


def main():
    with open("day13/input.txt") as f:
        s = f.read()
    now, busses = parse(s)
    print("Result:", compute(now, busses))

if __name__ == "__main__":
    test()
    main()
