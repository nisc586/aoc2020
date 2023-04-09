import re

EXAMPLE = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

MASK_RE = r"^mask = ([X10]{36})$"
MEM_RE = r"^mem\[(\d+)\] = (\d+)$"

def parse(s):
    ret = []
    for line in s.splitlines():
        mo = re.match(MASK_RE, line)
        if mo:
            or_mask = int(mo.group(1).replace("X", "0"), 2)
            xs = [len(mo.group(1)) - 1 - m.start() for m in re.finditer("X", mo.group(1))]
            ret.append(("mask", (or_mask, xs)))
            continue
        mo = re.match(MEM_RE, line)
        if mo:
            index = int(mo.group(1))
            value = int(mo.group(2))
            ret.append(("mem", (index, value)))
            continue
        raise(AssertionError(f"No match in {line=}"))
    return ret


def get_addresses(address, masks):
    or_mask, xs = masks
    n = len(xs)
    address |= or_mask  # set address bits to 1 where mask is 1
    result = []
    for insert_bits in range(2**n):
        altered_address = address
        for i in range(n):
            # Replace the Xs
            bit = get_bit(insert_bits, i)
            altered_address = set_bit(altered_address, xs[i], bit)
        result.append(altered_address)
    return result


def get_bit(n, bit_index):
    return (n >> bit_index) & 1

def set_bit(n, bit_index, value):
    if value:
        return n | (1 << bit_index)
    else:
        return n & ~(1 << bit_index)


def compute(ls):
    memory = {}
    mask = 0

    for op, args in ls:
        if op == "mask":
            mask = args
        elif op == "mem":
            index, value = args
            addresses = get_addresses(index, mask)
            for a in addresses:
                memory[a] = value
    return sum(memory.values())


def test():
    ops = parse(EXAMPLE)
    assert compute(ops) == 208


def main():
    with open("day14/input.txt") as f:
        ops = parse(f.read())
    print(compute(ops))


if __name__ == "__main__":
    test()
    main()
