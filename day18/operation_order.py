# Problem description
"""Math homework
Operator precedence has changed.
- addition and multiplication have the same precedence
- parentheses still change the order
"""

import pyparsing as pp
from operator import add, mul

number = pp.Char(pp.nums).setParseAction(lambda toks: int(toks[0]))
expr = pp.infixNotation(
    number,
    [(pp.oneOf("+ *"), 2, pp.opAssoc.LEFT)]
)

# Examples
# expr.runTests(
# """\
# 1 + 2 * 3 + 4 * 5 + 6
# 2 * 3 + (4 * 5)
# 5 + (8 * 3 + 9 + 3 * 4 * 3)
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
# """
# )


def evaluate(toks):
    if isinstance(toks[0], list):
        result = evaluate(toks.pop(0))
    else:
        result = toks.pop(0)
    while toks:
        op = toks.pop(0)
        if op == '+':
            if isinstance(toks[0], list):
                result += evaluate(toks.pop(0))
            else:
                result += toks.pop(0)
        elif op == '*':
            if isinstance(toks[0], list):
                result *= evaluate(toks.pop(0))
            else:
                result *= toks.pop(0)
    return result


def solve_line(s):
    toks = expr.parseString(s).asList()
    result = evaluate(toks)
    return result


def solve():
    file = "day18/input.txt"
    with open(file) as f:
        total = 0
        for line in f:
            total += solve_line(line)
    print(total)

def test():
    assert solve_line("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert solve_line("2 * 3 + (4 * 5)") == 26
    assert solve_line("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert solve_line("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert solve_line("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632

if __name__ == "__main__":
    solve()
