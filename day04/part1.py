import re
EXAMPLE = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

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
    required_fields = {
        "iyr",  # Issue Year
        "byr",  # Birth Year
        "eyr",  # Expiration Year
        "hgt",  # Height
        "hcl",  # Hair Color
        "ecl",  # Eye Color
        "pid",  # Passport ID
    }
    return sum(
        required_fields <= set(p)
        for p in passports
    )



def main():
    with open("day04/input.txt") as f:
        s = f.read()
    print(solve(s))


if __name__ == "__main__":
    assert solve(EXAMPLE) == 2
    main()