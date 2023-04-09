"""Memory game
- speak a sequence of starting numbers
- afterwards consinder the most recently spoken number n
    - if n was not spoken before -> say 0
    - else say turn - when n was last spoken
"""
import pytest


def solve(ls, limit=2020):
    # First round
    turn = 1
    n = ls[0]
    memory = {}

    while turn < limit:
        # print(f"{turn=}: {n=}")
        turn += 1

        prev = n
        if prev not in memory:
            n = 0
        else:
            n = turn-1 - memory[prev]
        memory[prev] = turn-1

        if turn <= len(ls):
            n = ls[turn-1]

    return n


@pytest.mark.parametrize("expected,arg", (
    (436, [0,3,6]),
    (1, [1,3,2]),
    (10, [2,1,3]),
    (27, [1,2,3]),
    (78, [2,3,1]),
    (438, [3,2,1]),
    (1836, [3,1,2])
))
def test_solve(expected, arg):
    assert expected == solve(arg)

@pytest.mark.parametrize("expected,arg", (
    (175594, [0,3,6]),
    (2578, [1,3,2]),
    (3544142, [2,1,3]),
    (261214, [1,2,3]),
    (6895259, [2,3,1]),
    (18, [3,2,1]),
    (362, [3,1,2])
))
def test_solve_limit(expected, arg):
    assert expected == solve(arg, limit=30_000_000)


if __name__ == "__main__":
    print(solve([1,20,11,6,12,0], limit=30_000_000))
