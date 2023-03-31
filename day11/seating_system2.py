from seating_system import Seatage


class Seatage2(Seatage):

    def occupied(self, j, i):
        """Returns the number of occupied seeds in linesight"""
        count = 0
        DIRECTIONS = (-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)
        for dx, dy in DIRECTIONS:
            row, col = tuple(((j+dx), (i+dy)))
            while 0 <= row < self.n and 0 <= col < self.m:

                if self.previous[row][col] == "#":
                    count += 1
                    break
                elif self.previous[row][col] == "L":
                    break

                row, col = tuple(((row+dx), (col+dy)))
        return count


def main():
    with open("day11/input.txt") as f:
        s = f.read()
    stg = Seatage2(s)
    while not stg.is_stable():
        stg.simulate(tolerance=5)
    print(stg.count_occupied(), "seats end up occupied")


if __name__ == "__main__":
    main()
