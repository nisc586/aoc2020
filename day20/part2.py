import itertools
import math
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


MONSTER = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

monster = {(i, j)
           for j, line in enumerate(MONSTER.splitlines())
           for i, c in enumerate(line)
           if c == "#"
           }

class Tile:
    def __init__(self, id, pixels):
        self.id = id
        self.pixels = pixels
        self._update_edges()
    
    def _update_edges(self):
        self.top = self.pixels[0]
        self.bottom = self.pixels[-1]
        self.left = tuple(row[0] for row in self.pixels)
        self.right = tuple(row[-1] for row in self.pixels)
    
    def get_edges(self):
        return {self.top, self.bottom, self.left, self.right}
    
    def can_combine_with(self, other_tile):
        other_edges = other_tile.get_edges()
        other_edges_reversed = {tup[::-1] for tup in other_edges}
        return len(self.get_edges().intersection(other_edges.union(other_edges_reversed))) > 0
    
    def turn(self):
        self.pixels = tuple(zip(*self.pixels[::-1]))
        self._update_edges()

    def flip(self):
        self.pixels = tuple(
            row[::-1] for row in self.pixels
        )
        self._update_edges()
    
    def get_image(self):
        return [
            [pixel for pixel in row[1:-1]]
            for row in self.pixels[1:-1]
        ]
    
    def __eq__(self, other_tile):
        return self.id == other_tile.id
    
    def __hash__(self):
        return hash(self.id)
    
    def __repr__(self):
        return f"Tile: {self.id}"


class Puzzle:
    def __init__(self, size, corner):
        self.tiles = {(0, 0): corner}
        self.size = size
        self.row = 0
        self.col = 1
    
    def inc_open_spot(self):
        if self.col < self.size-1:
            self.col +=1
        else:
            self.row += 1
            self.col = 0
    
    def tile_fits(self, tile):
        """Check if a tile fits the next free spot."""
        row, col = self.row, self.col
        result = True
        if (row-1, col) in self.tiles:
            result &= self.tiles[row-1, col].bottom == tile.top
        if (row+1, col) in self.tiles:
            result &= self.tiles[(row+1, col)].top == tile.bottom
        if (row, col-1) in self.tiles:
            result &= self.tiles[(row, col-1)].right == tile.left
        if (row, col+1) in self.tiles:
            result &= self.tiles[(row, col+1)].left == tile.right
        return result
    
    def add_tile(self, tile):
        """Add a tile to the next free spot."""
        if self.tile_fits(tile):
            self.tiles[(self.row, self.col)] = tile
            self.inc_open_spot()
        else:
            raise AssertionError(f"Tile {tile.id} does not fit at {self.row=}, {self.col=}")
    
    def get_image(self):
        image = []
        for i in range(self.size):
            row = [self.tiles[(i, j)].get_image() for j in range(self.size)]
            for k in range(len(row[0])):
                image.append([pixel for pixel in itertools.chain(*[segment[k] for segment in row])])
        return image


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


def find_corners(tiles):
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

def make_top_left(corner, tiles):
    left_correct = (
        all(corner.left not in other.get_edges() for other in tiles)
        and
        all(corner.left[::-1] not in other.get_edges() for other in tiles)
    )
    top_correct = (
        all(corner.top not in other.get_edges() for other in tiles)
        and
        all(corner.top[::-1] not in other.get_edges() for other in tiles)
    )
    if left_correct and not top_correct:
        corner.turn()
    elif not left_correct and not top_correct:
        corner.turn()
        corner.turn()
    elif not left_correct and top_correct:
        corner.turn()
        corner.turn()
        corner.turn()


def solve_puzzle(tiles):
    size = int(math.sqrt(len(tiles)))

    corner = find_corners(tiles).pop()
    tiles.remove(corner)
    make_top_left(corner, tiles)
    puzzle = Puzzle(size, corner)

    while tiles:
        some_tile = tiles.pop(0)

        if puzzle.tile_fits(some_tile):
            puzzle.add_tile(some_tile)
            continue
        
        some_tile.turn()
        if puzzle.tile_fits(some_tile):
            puzzle.add_tile(some_tile)
            continue

        some_tile.turn()
        if puzzle.tile_fits(some_tile):
            puzzle.add_tile(some_tile)
            continue

        some_tile.turn()
        if puzzle.tile_fits(some_tile):
            puzzle.add_tile(some_tile)
            continue

        some_tile.turn()
        some_tile.flip()
        tiles.append(some_tile)
    
    return puzzle


def scan_image(image, pattern):
    image_size = len(image)
    pattern_width = max(x for x,_ in pattern)
    pattern_height = max(y for _, y in pattern)

    matches = 0
    for i in range(image_size - pattern_width):
        for j in range(image_size - pattern_height):
            offset = (i, j)
            matches += all(
                image[i+x][j+y]
                for (x, y) in pattern
            )
    return matches


def turn_image(image):
    return list(zip(*image[::-1]))


def flip_image(image):
    return list(row[::-1] for row in image)


def find_monster(image):    
    n = scan_image(image, monster)

    image = turn_image(image)
    n = max(scan_image(image, monster), n)

    image = turn_image(image)
    n = max(scan_image(image, monster), n)

    image = turn_image(image)
    n = max(scan_image(image, monster), n)

    image = flip_image(turn_image(image))
    n = max(scan_image(image, monster), n)

    image = turn_image(image)
    n = max(scan_image(image, monster), n)

    image = turn_image(image)
    n = max(scan_image(image, monster), n)

    image = turn_image(image)
    n = max(scan_image(image, monster), n)

    return n
    
def test():
    tiles = parse(EXAMPLE)
    p = solve_puzzle(tiles)
    image = p.get_image()
    n = find_monster(image)
    assert n == 2
    roughness = sum(x for row in image for x in row) - len(monster) * n
    assert roughness == 273, f"actual: {roughness=}"


def solve(s):
    tiles = parse(s)
    p = solve_puzzle(tiles)
    image = p.get_image()
    n = find_monster(image)
    roughness = sum(x for row in image for x in row) - len(monster) * n
    return roughness


def main():
    with open("day20/input.txt") as f:
        s = f.read()
    print(solve(s))


if __name__ == "__main__":
    test()
    main()