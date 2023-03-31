import pytest
from seating_system import Seatage

STATE0 = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL\
"""

STATE1 = """\
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##\
"""

STATE2 = """\
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##\
"""

STATE3 = """\
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##\
"""

STATE4 = """\
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##\
"""

STATE5 = """\
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##\
"""

def test_simulate():
    stg = Seatage(STATE0)
    stg.simulate()
    assert str(stg) == STATE1
    stg.simulate()
    assert str(stg) == STATE2
    stg.simulate()
    assert str(stg) == STATE3
    stg.simulate()
    assert str(stg) == STATE4

def test_is_stable():
    stg = Seatage(STATE5)
    stg.simulate()
    assert stg.is_stable()

def test_str():
    stg = Seatage(STATE0)
    assert str(stg) == STATE0
    stg = Seatage(STATE3)
    assert str(stg) == STATE3

def test_count_occupied():
    stg = Seatage(STATE5)
    assert  37 == stg.count_occupied()

if __name__ == "__main__":
    pytest.main()
