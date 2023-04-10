from collections import defaultdict
from itertools import product
import math

EXAMPLE = """\
.#.
..#
###"""

PUZZLE_INPUT="""\
##....#.
#.#..#..
...#....
...#.#..
###....#
#.#....#
.#....##
.#.###.#"""

class PocketDimension:
    def __init__(self, input_s):
        self.state = defaultdict(int)

        lines = input_s.splitlines()
        self.size = (len(lines) - 1) // 2

        for i, line in enumerate(lines):
            y = i - self.size
            for j, cube in enumerate(line):
                x = j - self.size
                if cube == "#":
                    self.state[(x, y, 0, 0)] = 1



    def print(self):

        for w in range(-self.size, self.size+1):
            for z in range(-self.size, self.size + 1):
                print(f"{w=} {z=}\n")
                for y in range(-self.size, self.size + 1):
                    for x in range(-self.size, self.size + 1):
                        print(self.state[(x, y, z, w)], end="")
                    print()
                print("\n")


    def cycle(self):

        new_state = defaultdict(int)

        for point, value in tuple(self.state.items()):
            adjacent_actives = self.get_active_neighbors(point)
            if value:
                new_state[point] = 1 if adjacent_actives in (2, 3) else 0

        for point, value in tuple(self.state.items()):
            adjacent_actives = self.get_active_neighbors(point)
            if not value:
                new_state[point] = 1 if adjacent_actives == 3 else 0

        self.size += 1
        self.state = new_state


    def get_neighbors(self, point):
        """Returns a list of points that count as a neighbor to point"""
        px, py, pz, pw = point
        return [
                    (x, y, z, w) 
                    for x, y, z, w in product((px-1, px, px+1), (py-1, py, py+1), (pz-1, pz, pz+1), (pw-1, pw, pw+1))
                    if not (x,y,z,w) == point
                ]


    def get_active_neighbors(self, point):
        """Returns the number of active neighbors of a cube at point."""

        active_neighbors = 0
        for p in self.get_neighbors(point):
            active_neighbors += self.state[p]
        
        return active_neighbors


if __name__ == "__main__":
    pd = PocketDimension(PUZZLE_INPUT)
    # pd.print()

    for reps in range(6):
        pd.cycle()

    print(sum(x for x in pd.state.values()))  # expect 848
