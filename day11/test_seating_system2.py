import pytest
from seating_system2 import Seatage2

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
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#\
"""

STATE3 = """\
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#\
"""

STATE4 = """\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#\
"""

STATE5 = """\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#\
"""

STATE6 = """\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#\
"""

def test_simulate():
    stg = Seatage2(STATE0)
    stg.simulate(tolerance=5)
    assert str(stg) == STATE1
    stg.simulate(tolerance=5)
    assert str(stg) == STATE2
    stg.simulate(tolerance=5)
    assert str(stg) == STATE3
    stg.simulate(tolerance=5)
    assert str(stg) == STATE4
    stg.simulate(tolerance=5)
    assert str(stg) == STATE5

def test_is_stable():
    stg = Seatage2(STATE6)
    stg.simulate(tolerance=5)
    assert stg.is_stable()

def test_str():
    stg = Seatage2(STATE0)
    assert str(stg) == STATE0
    stg = Seatage2(STATE3)
    assert str(stg) == STATE3

def test_count_occupied():
    stg = Seatage2(STATE6)
    assert  26 == stg.count_occupied()

if __name__ == "__main__":
    pytest.main()
