import re
from collections import Counter

EXAMPLE = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""

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
        count = Counter()
        while stack:
            rule_number = stack.pop()

            # prevent a loop
            count[rule_number] += 1
            

            number_pattern = rf"\b{rule_number}\b"
            for idx, rule in enumerate(self.rules):
                
                if re.search(number_pattern, rule):
                    expanded_rule = re.sub(number_pattern, f"({self.rules[rule_number]})", rule)
                    self.rules[idx] = expanded_rule
                    if count[idx] < 4:
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
    assert d.count_matches(messages) == 3, f"expected: 3, got: {d.count_matches(messages)}"


def test_updated():
    rules, messages = parse(EXAMPLE)
    rules = sorted(rules)
    rules.append("8: 42 | 42 8")
    rules.append("11: 42 31 | 42 11 31")
    d = Decoder(rules)
    assert d.count_matches(messages) == 12, f"expected: 12, got: {d.count_matches(messages)}" 


def main():
    with open("day19/input.txt") as f:
        s = f.read()
    rules, messages = parse(s)
    rules.append("8: 42 | 42 8")
    rules.append("11: 42 31 | 42 11 31")
    d = Decoder(rules)
    print(d.count_matches(messages))


if __name__ == "__main__":
    test()
    test_updated()
    main()
