from math import prod
import re

EXAMPLE = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""

class Tile:
    def __init__(self, id, pixels):
        self.id = id
        self.pixels = pixels
    
    def get_edges(self):
        return {
        self.pixels[0],  # top
        self.pixels[-1],  # bottom
        tuple(row[0] for row in self.pixels),  # left
        tuple(row[-1] for row in self.pixels),  # right
        }
    
    def can_combine_with(self, other_tile):
        other_edges = other_tile.get_edges()
        other_edges_reversed = {tup[::-1] for tup in other_edges}
        return len(self.get_edges().intersection(other_edges.union(other_edges_reversed))) > 0


def parse(s):
    tiles = []
    for piece in s.split("\n\n"):
        if piece == "": continue
        lines = piece.splitlines()
        id = int(re.match(r"Tile (\d+):", lines[0]).group(1))
        pixels = tuple(
            tuple(int(c=="#") for c in line)
            for line in lines[1:]
        )
        tiles.append(Tile(id, pixels))
    return tiles


def find_corner_pieces(tiles):
    corners = set()
    for i, tile in enumerate(tiles):
        n_matching_pieces = sum(
            tile.can_combine_with(other_tile)
            for j, other_tile in enumerate(tiles)
            if i != j
        )
        if n_matching_pieces == 2:
            corners.add(tile)
    return corners


def solve(s):
    tiles = parse(s)
    corners = find_corner_pieces(tiles)
    return prod(tile.id for tile in corners)


def test():
    actual = solve(EXAMPLE)
    expected = 20899048083289
    assert expected == actual, f"expected: {expected} but got: {actual}"

def main():
    with open("day20/input.txt") as f:
        s = f.read()
    print(solve(s))

if __name__ == "__main__":
    test()
    main()