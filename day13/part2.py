EXAMPLE = """939
7,13,x,x,59,x,31,19"""

def parse(s):
    lines = s.splitlines()
    ret = []
    for token in lines[1].split(","):
        try:
            ret.append(int(token))
        except ValueError:
            ret.append(None)
    return ret

def extended_gcd_recursive(a, b):
    """Calculate s and t so the equation gcd(a,b) = s*a + t*b is fulfilled"""
    if b==0:
        return 1, 0
    else:
        q = a // b
        r = a % b
        s_old, t_old = extended_gcd_recursive(b, r)
        s = t_old
        t = s_old - q*t_old
        return s, t


def chinese_remainder(*a_m_pairs):
    M = 1
    for a, m in a_m_pairs:
        M *= m
    x = 0
    for a, m in a_m_pairs:
        M_i = M // m
        r, s = extended_gcd_recursive(m, M_i)
        x += a * s * M_i
    return x % M


def compute(ls):
    args = []
    for a, m in enumerate(ls):
        if m:
            args.append((-a % m, m))
    print(chinese_remainder(*args))


def main():
    with open("day13/input.txt") as f:
        s = f.read()
    ins = parse(s)
    compute(ins)

if __name__ == "__main__":
    main()
    # print(extended_gcd_recursive(78, 99))  # expect (14, -11)
    # print(chinese_remainder((2,3), (3, 4), (2, 5)))  # expect 47
    # print(compute(INPUT))  # expect 1068781
    # print(compute( [17, None, 13, 19] ))  # expect 3417
    # print(compute( [67, 7, 59, 61] ))  # expect 754018
    # print(compute( [67, None, 7, 59, 61] ))  # expect 779210
    # print(compute( [1789, 37, 47, 1889] ))  # expect 1202161486
