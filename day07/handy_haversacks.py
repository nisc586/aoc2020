import re

EXAMPLE = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

def parse(s):
	graph = {}
	for line in s.splitlines():
		pattern1 = r"(?P<container>\w+ \w+) bags contain"
		container = re.match(pattern1, line).group("container")
		pattern2 = r"(?P<count>\d) (?P<color>\w+ \w+) (?:bags|bag)"
		contents = [(int(c), col) for c, col in re.findall(pattern2, line)]
		graph[container] = contents
	return graph


def solve(s):
	graph = parse(s)
	result = set()
	stack = ["shiny gold"]
	while stack:
		searched_color = stack.pop()
		for container in graph.keys():
			for count, content in graph[container]:
				if content == searched_color:
					result.add(container)
					stack.append(container)
	return len(result)

def main():
	with open("day07/input.txt") as f:
		s = f.read()
	print(solve(s))

if __name__ == "__main__":
	assert solve(EXAMPLE) == 4, f"expected: 4 but got: {solve(EXAMPLE)}"
	main()
