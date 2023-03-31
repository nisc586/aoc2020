from copy import deepcopy
import itertools


class Seatage:
    """Simulates seats in a waiting area.

    seats: list of lists.
    n: number of rows
    m: number of columns

    Index starts at 0 (top left). seats[1][0] is second row, first column.
    """


    def __init__(self, s):
        self.seats = [list(line) for line in s.splitlines()]
        self.previous = None
        self.n = len(self.seats)
        self.m = len(self.seats[0])


    def simulate(self, tolerance=4):
        self.previous = deepcopy(self.seats)
        for j, i in itertools.product(range(self.n), range(self.m)):
            # Rule 1: If seat is empty and there are no adjacent seats occupied it becomes occupied
            if self.previous[j][i] == "L" and self.occupied(j, i) == 0:
                self.seats[j][i] = "#"
            # Rule 2: If seat is occupied and four or more adjacent seats are also occupied it becomes empty
            if self.previous[j][i] == "#" and self.occupied(j, i) >= tolerance:
                self.seats[j][i] = "L"


    def occupied(self, j, i):
        ADJACENT = (j-1, i-1), (j-1, i), (j-1, i+1), (j, i-1), (j, i+1), (j+1, i-1), (j+1, i), (j+1, i+1)
        count = 0
        for row, col in ADJACENT:
            if 0 <= row < self.n and 0 <= col < self.m:
                if self.previous[row][col] == "#":
                    count += 1
        return count


    def is_stable(self):
        return self.previous == self.seats


    def __str__(self):
        lines = ["".join(row) for row in self.seats]
        return "\n".join(lines)


    def count_occupied(self):
        count = 0
        for i, j in itertools.product(range(self.n), range(self.m)):
            if self.seats[i][j] == "#":
                count += 1
        return count


def main():
    with open("day11/input.txt") as f:
        s = f.read()
    stg = Seatage(s)
    while not stg.is_stable():
        stg.simulate()
    print(stg.count_occupied(), "seats end up occupied")


if __name__ == "__main__":
    main()
