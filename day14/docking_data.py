import re
from collections import defaultdict

EXAMPLE = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

MASK_RE = r"^mask = ([X10]{36})$"
MEM_RE = r"^mem\[(\d+)\] = (\d+)$"

def parse(s):
    ret = []
    for line in s.splitlines():
        mo = re.match(MASK_RE, line)
        if mo:
            mask_on = int(mo.group(1).replace("X", "0"), 2)
            mask_off = int(mo.group(1).replace("X", "1"), 2)
            ret.append(("mask", (mask_on, mask_off)))
            continue
        mo = re.match(MEM_RE, line)
        if mo:
            index = int(mo.group(1))
            value = int(mo.group(2))
            ret.append(("mem", (index, value)))
            continue
        raise(AssertionError(f"No match in {line=}"))
    return ret

def compute(ls):
    memory = defaultdict(int)
    mask_on, mask_off = 0, 0

    for op, (arg1, arg2) in ls:
        if op == "mask":
            mask_on = arg1
            mask_off = arg2
        elif op == "mem":
            index = arg1
            value = arg2
            result = value & mask_off | mask_on
            memory[index] = result
        else:
            raise(AssertionError("unreachable"))
    return memory


def test():
    ins = parse(EXAMPLE)
    actual = sum(compute(ins).values())
    assert 165 == actual


def main():
    with open("day14/input.txt") as f:
        ins = parse(f.read())
    result = sum(compute(ins).values())
    print("Sum of values in memory is", result)


if __name__ == "__main__":
    test()
    main()
