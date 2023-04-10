import re
from collections import namedtuple

# x direction is towards "e"
# y direction is towards "ne"
Position = namedtuple("Position", ["x", "y"])

EXAMPLE = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

def parse(s):
    pattern = r"e|se|sw|w|nw|ne"
    return re.findall(pattern, s)


def get_relative_position(directions):
    relative_position = Position(0, 0)
    for direction in directions:
        if direction == "e":
            relative_position = Position(relative_position.x+1, relative_position.y)
        elif direction == "se":
            relative_position = Position(relative_position.x+1, relative_position.y-1)
        elif direction == "sw":
            relative_position = Position(relative_position.x, relative_position.y-1)
        elif direction == "w":
            relative_position = Position(relative_position.x-1, relative_position.y)
        elif direction == "nw":
            relative_position = Position(relative_position.x-1, relative_position.y+1)
        elif direction == "ne":
            relative_position = Position(relative_position.x, relative_position.y+1)
    return relative_position

def initial_black_tiles(s):
    black_tiles = set()
    for line in s.splitlines():
        directions = parse(line)
        flip_tile = get_relative_position(directions)
        if flip_tile in black_tiles:
            black_tiles.remove(flip_tile)
        else:
            black_tiles.add(flip_tile)
    return black_tiles

def get_neighbors(position):
    return {
        Position(position.x+1, position.y),  # e
        Position(position.x-1, position.y),  # w
        Position(position.x, position.y+1),  # ne
        Position(position.x, position.y-1),  # sw
        Position(position.x-1, position.y+1),  # nw
        Position(position.x+1, position.y-1),  # se
    }

def update(black_tiles):
    new_black_tiles = set()

    for tile in black_tiles:
        adjacent_black_tiles = get_neighbors(tile) & black_tiles
        if (len(adjacent_black_tiles) in (1, 2)):
            # tile stays black if it has 1 or 2 black adjacent tiles
            new_black_tiles.add(tile)

        adjacent_white_tiles = get_neighbors(tile) - black_tiles
        for white_tile in adjacent_white_tiles:
            if (len(get_neighbors(white_tile) & black_tiles) == 2):
                # white tile has 2 black adjacent tiles
                new_black_tiles.add(white_tile)

    return new_black_tiles

def solve(s):
    black_tiles = initial_black_tiles(s)
    result = []
    for day in range(100):
        black_tiles = update(black_tiles)
        result.append(len(black_tiles))
    return result

def test():
    actual = solve(EXAMPLE)
    assert actual[:10] == [15, 12, 25, 14, 23, 28, 41, 37, 49, 37]
    assert actual[19] == 132
    assert actual[29] == 259
    assert actual[39] == 406
    assert actual[99] == 2208

def main():
    with open("day24/input.txt") as f:
        s = f.read()
    print(solve(s)[-1])

if __name__ == "__main__":
    test()
    main()

