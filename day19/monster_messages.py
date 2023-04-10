import re
EXAMPLE = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

class Decoder:
    def __init__(self, rule_lines):
        self.rules = [""] * 200
        self.base_rules = []

        for line in rule_lines:
            m = re.match(r"^(\d+): (.*)$", line)
            i = int(m.group(1))
            pattern = m.group(2)
            if re.match(r'"a"', pattern):
                pattern = "a"
                self.base_rules.append(i)
            elif re.match(r'"b"', pattern):
                pattern = "b"
                self.base_rules.append(i)

            self.rules[i] = pattern
        
        self.expand_rules()


    def expand_rules(self):
        stack = self.base_rules[:]

        while stack:
            rule_number = stack.pop()
            number_pattern = rf"\b{rule_number}\b"
            for idx, rule in enumerate(self.rules):
                if re.search(number_pattern, rule):
                    expanded_rule = re.sub(number_pattern, f"({self.rules[rule_number]})", rule)
                    self.rules[idx] = expanded_rule
                    stack.append(idx)


    def count_matches(self, messages, i=0):
        pattern = f"^{self.rules[i]}$"
        return sum(
            1
            for message in messages
            if re.match(pattern, message, re.VERBOSE)
        )
    

def parse(s):
    rules_text, messages_text = s.split("\n\n")

    rules = rules_text.splitlines()
    messages = messages_text.splitlines()
    return rules, messages


def test():
    rules, messages = parse(EXAMPLE)
    d = Decoder(rules)
    assert d.count_matches(messages) == 2, f"expected: 2, got: {d.count_matches(messages)}"


def main():
    with open("day19/input.txt") as f:
        s = f.read()
    rules, messages = parse(s)
    d = Decoder(rules)
    print(d.count_matches(messages))


if __name__ == "__main__":
    test()
    main()
