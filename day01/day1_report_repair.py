"""Find the two and three numbers that sum up to 2020.

Example array:
1721 979 366 299 675 1456

1721 + 299 = 2020
979 + 366 + 675 = 2020
Multiply them for the answer.
"""


def find_two(nums, s=2020):
    """\
Finds two numbers in a list that sum up to s and returns their product.

>>> find_two([1721,979,366,299,675,1456])
514579
"""
    seen = set()
    for n in nums:
        if s-n in seen:
            return (s-n)*n
        else:
            seen.add(n)


def find_three(nums):
    """\
Finds three numbers in a list that sum up to 2020 and returns their product.

>>> find_three([1721,979,366,299,675,1456])
241861950
"""
    for i, num in enumerate(nums):
        two_prod = find_two(nums[:i] + nums[i+1:], s=2020-num)
        if two_prod:
            return two_prod * num


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    with open(r"day01/input.txt", "r") as f:
        numbers = [int(ln) for ln in f.readlines()]

    print(find_three(numbers))
