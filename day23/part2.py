EXAMPLE = "389125467"

def parse(s):
    # linked is like a forward linked list
    # each key points to the label of the cup after it
    # the last cup points to the first cup
    nums = [int(c) for c in s]

    linked = {
        num: nums[i+1]
        for i, num in enumerate(nums[:-1])
    }   

    linked[nums[-1]] = len(nums) + 1

    for i in range(len(nums)+1, 1_000_000):
        linked[i] = i+1
    linked[1_000_000] = nums[0]

    return linked


def solve(s, moves):
    points_to = parse(s)
    n = len(points_to)
    
    current = int(s[0])

    for reps in range(moves):
        # move starts here
        # remove 3
        first = points_to[current]
        second = points_to[first]
        third = points_to[second]

        points_to[current] = points_to[third]

        # find destination
        destination = current - 1
        if destination == 0:
            destination = n
        
        while destination in {first, second, third}:
            destination -= 1
            if destination == 0:
                destination = n

        # insert at destination
        points_to[third] = points_to[destination]
        points_to[destination] = first

        # update current cup
        current = points_to[current]

    a = points_to[1]
    b = points_to[a]
    return a, b


def test():
    actual = solve(EXAMPLE, 10_000_000)
    assert actual == (934001, 159792), f"{actual}"


def main():
    a, b = solve("952438716", 10_000_000)
    print(a * b)


if __name__ == "__main__":
    test()
    main()