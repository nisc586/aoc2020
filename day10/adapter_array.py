from collections import Counter

def parse(s):
    return sorted(int(line) for line in s.splitlines())

def compute(adapters):
    counts = Counter({3: 1})
    current_jolts = 0

    # Greedy algorithm: use smallest adapter first
    for val in adapters:
        difference = val - current_jolts
        if 1 <= difference <= 3:
            current_jolts = val
            counts[difference] += 1

    return counts[3] * counts[1]

def main():
    with open("day10/input.txt") as f:
        adapters = parse(f.read())
    print("Result problem 1:", compute(adapters))

if __name__ == "__main__":
    main()
