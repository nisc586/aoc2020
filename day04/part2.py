import re
EXAMPLE1 = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

EXAMPLE2 = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

def parse(s):
    pattern = r"(\w{3}):([#a-z0-9]+)"
    result = []
    for fields in s.split("\n\n"):
        passport = {}
        for match in re.finditer(pattern, fields):
            passport[match.group(1)] = match.group(2)
        result.append(passport)
    return result

def solve(s):
    passports = parse(s)
    
    return sum(
        is_valid(p)
        for p in passports
    )


def is_valid(passport):
    required_fields = {
        "iyr",  # Issue Year
        "byr",  # Birth Year
        "eyr",  # Expiration Year
        "hgt",  # Height
        "hcl",  # Hair Color
        "ecl",  # Eye Color
        "pid",  # Passport ID
    }
    if (not (required_fields <= set(passport))): return False

    return all([
        1920 <= int(passport["byr"]) <= 2002,
        2010 <= int(passport["iyr"]) <= 2020,
        2020 <= int(passport["eyr"]) <= 2030,
        is_valid_hgt(passport["hgt"]),
        re.match(r"^#[a-f0-9]{6}$", passport["hcl"]),
        passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        re.match(r"^\d{9}$", passport["pid"]),
    ])


def is_valid_hgt(s):
    pattern = r"(\d+)(in|cm)"
    m = re.match(pattern, s)
    if not m: return False
    
    n, unit = int(m.group(1)), m.group(2)
    
    if unit == "in":
        return 59 <= n <= 79
    elif unit == "cm":
        return 150 <= n <= 193


def main():
    with open("day04/input.txt") as f:
        s = f.read()
    print(solve(s))


if __name__ == "__main__":
    assert solve(EXAMPLE1) == 0
    assert solve(EXAMPLE2) == 4
    main()