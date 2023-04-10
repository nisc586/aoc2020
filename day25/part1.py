def transform(subject_number, loop_size):
    CONST = 20201227
    value = 1
    transforms = [value]
    for _ in range(loop_size):
        value = (value * subject_number) % CONST
        transforms.append(value)
    return transforms


def compute(card_public_key, door_public_key):
    N = 10_000_000
    initial_subject_number = 7
    
    initial_transforms = transform(initial_subject_number, N)
    
    card_loop_size = initial_transforms.index(card_public_key)
    card_encryption_key = transform(door_public_key, card_loop_size)[-1]
    return card_encryption_key


def test():
    assert compute(card_public_key=5764801, door_public_key=17807724) == 14897079


def main():
    with open("day25/input.txt") as f:
        s = f.read()
    card_public, door_public = [int(line) for line in s.splitlines()]
    print(compute(card_public, door_public))


if __name__ == "__main__":
    test()
    main()