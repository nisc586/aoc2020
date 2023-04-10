import re
from collections import namedtuple

# x direction is towards "e"
# y direction is towards "ne"
# every direction can be expressed as a combination of x and y
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

def solve(s):
    black_tiles = set()
    for line in s.splitlines():
        directions = parse(line)
        flip_tile = get_relative_position(directions)
        if flip_tile in black_tiles:
            black_tiles.remove(flip_tile)
        else:
            black_tiles.add(flip_tile)
    return len(black_tiles)


def test_parse():
    assert parse("esew") == ['e', 'se', 'w']
    assert parse("nwwswee") == ['nw', 'w', 'sw', 'e', 'e']


def test_get_relative_position():
    assert get_relative_position(['e', 'se', 'w']) == Position(1, -1)
    assert get_relative_position(['nw', 'w', 'sw', 'e', 'e']) == Position(0, 0)


def test():
    assert solve(EXAMPLE) == 10

def main():
    with open("day24/input.txt") as f:
        s = f.read()
    print(solve(s))

if __name__ == "__main__":
    test_parse()
    test_get_relative_position()
    test()
    main()

