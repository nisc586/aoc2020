import re

EXAMPLE = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


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
	my_bag_color = "shiny gold"
	return count_content(my_bag_color, graph)


def count_content(color, graph):
	total = 0
	for n, col in graph[color]:
		total += n * (1 + count_content(col, graph))
	return total


def main():
	with open("day07/input.txt") as f:
		s = f.read()
	print(solve(s))


if __name__ == "__main__":
	assert solve(EXAMPLE) == 126
	main()