from collections import defaultdict
import re

EXAMPLE = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""


RULE_RE = r"^(.*): (\d+)-(\d+) or (\d+)-(\d+)$"


def parse(s):
    """Returns a 3-tuple, first is a list of rules, second is my ticket, third is list of nearby tickets"""
    rule_part, my_ticket_part, nearby_tickets_part = s.split(
        "\n\n", maxsplit=3)
    rules = parse_rules(rule_part)
    my_ticket = parse_tickets(my_ticket_part)[0]
    nearby_tickets = parse_tickets(nearby_tickets_part)
    return rules, my_ticket, nearby_tickets


def parse_rules(s):
    rules = {}
    for line in s.splitlines():
        mo = re.match(RULE_RE, line)
        rules[mo[1]] = int(mo[2]), int(mo[3]), int(mo[4]), int(mo[5])
    return rules


def parse_tickets(s):
    lines = s.splitlines()[1:]  # skip first line
    return [[int(i) for i in line.split(",")] for line in lines]


def scanning_error_rate(tickets, rules):
    error_rate = 0
    for ticket in tickets:
        for number in ticket:
            if not is_valid(number, rules):
                error_rate += number
    return error_rate


def is_valid(n, rules):
    for min1, max1, min2, max2 in rules:
        if min1 <= n <= max1 or min2 <= n <= max2:
            return True
    return False


def test():
    rules, _, nearby_tickets = parse(EXAMPLE)
    assert scanning_error_rate(nearby_tickets, rules.values()) == 71


def main():
    with open("day16/input.txt") as f:
        rules, my_ticket, nearby_tickets = parse(f.read())
    print(scanning_error_rate(nearby_tickets, rules.values()))


if __name__ == "__main__":
    test()
    main()
