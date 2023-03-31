import pytest
from adapter_array import compute
from adapter_array_part2 import chain, arrangements

INPUT = [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
INPUT2 =[1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24\
    , 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49]


def test_compute():
    assert 35 == compute(INPUT)
    assert 220 == compute(INPUT2)


def test_make_chain():
    assert sorted(INPUT) == chain(INPUT)
    assert sorted(INPUT2) == chain(INPUT2)


@pytest.mark.parametrize("expected,test_input", [(8, INPUT), (19208, INPUT2)])
def test_arrangements(expected, test_input):
    assert expected == arrangements(test_input)


if __name__ == "__main__":
    pytest.main()
