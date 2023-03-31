from collections import defaultdict

INPUT = [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
INPUT2 =[1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24\
    , 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49]



def parse(s):
    return sorted(int(line) for line in s.splitlines())


def chain(adapters):
    ret = []
    current_jolts = 0

    # Greedy algorithm: use smallest adapter first
    for val in adapters:
        difference = val - current_jolts
        if 1 <= difference <= 3:
            current_jolts = val
            ret.append(val)
    return ret


def arrangements(chain):
    combs = defaultdict(int, {0: 1})
    for n in chain:
        combs[n] = combs[n-1] + combs[n-2] + combs[n-3]
    return combs[chain[-1]]


def main():
    with open("day10/input.txt") as f:
        ins = chain(parse(f.read()))
    print(arrangements(ins))


if __name__ == "__main__":
    main()
