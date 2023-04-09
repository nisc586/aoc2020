from collections import defaultdict
import re

EXAMPLE = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""


RULE_RE = r"^(.*): (\d+)-(\d+) or (\d+)-(\d+)$"

def parse(s):
    """Returns a 3-tuple, first is a list of rules, second is my ticket, third is list of nearby tickets"""
    rule_part, my_ticket_part, nearby_tickets_part = s.split("\n\n", maxsplit=3)
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
    lines = s.splitlines()[1:] # skip first line
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


def is_inbounds(n, limits):
    min1, max1, min2, max2 = limits
    return min1 <= n <= max1 or min2 <= n <= max2


def is_valid_ticket(ticket, rules):
    """True if all numbers in ticket can fullfill any rule"""
    return all([
        any([
            is_inbounds(n, limits)
            for limits in rules.values()
            ]) 
        for n in ticket])


def main():
    with open("day16/input.txt") as f:
        rules, my_ticket, nearby = parse(f.read())

    tickets = [my_ticket] + [t for t in nearby if is_valid_ticket(t, rules)]
    assert scanning_error_rate(tickets, rules.values()) == 0


    possible_fields = defaultdict(set)
    for field, limits in rules.items():
        for j in range(len(my_ticket)):
            column = [ticket[j] for ticket in tickets]

            if all([is_inbounds(n, limits) for n in column]):
                possible_fields[j].add(field)


    positions = {}
    while possible_fields:
        for pos, fields in tuple(possible_fields.items()):
            if len(fields) == 1:
                del possible_fields[pos]
                field = fields.pop()
                positions[field] = pos
                for v in possible_fields.values():
                    v.discard(field)

    total = 1
    for field, pos in positions.items():
        if field.startswith("departure"):
            total *= my_ticket[pos]

    print("Solution of part 2 is:", total)


if __name__ == "__main__":
    main()
