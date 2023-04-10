EXAMPLE = "389125467"

def parse(s):
    return [int(c) for c in s]


def solve(s, moves):
    cups = parse(s)
    n = len(cups)

    current_cup = cups[0]

    for reps in range(moves):
        current_cup = cups[0]
        pick_up_cups = cups[1:4]
        del cups[1:4]

        destination_cup = current_cup - 1
        if destination_cup == 0:
            destination_cup = n
        while destination_cup in pick_up_cups:
            destination_cup = destination_cup - 1
            if destination_cup == 0:
                destination_cup = n

        while cups[-1] != destination_cup:
            cups.append(cups.pop(0))

        cups.extend(pick_up_cups)

        while cups[0] != current_cup:
            cups.append(cups.pop(0))
        cups.append(cups.pop(0))

    while cups[0] != 1:
        cups.append(cups.pop(0))
    return "".join(str(x) for x in cups[1:])


def test():
    assert solve(EXAMPLE, 10) == "92658374"
    assert solve(EXAMPLE, 100) == "67384529"


def main():
    print(solve("952438716", 100))


if __name__ == "__main__":
    test()
    main()