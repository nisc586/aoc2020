# example = """\
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#"""
# grid = [list(row) for row in example.split("\n")]

def count_trees(grid, start, slope, width, height):

	pointer_x, pointer_y = start
	slope_x, slope_y = slope

	tree_count = 0
	while True:
		pointer_x = pointer_x + slope_x
		pointer_y = (pointer_y + slope_y) % width
		if pointer_x >= height:
			break
		else:
			if grid[pointer_x][pointer_y] == "#":
				tree_count += 1

	return tree_count


def main():
	with open(r"day03/input.txt") as f:
		grid = [list(row.strip()) for row in f]

	height = len(grid)
	width = len(grid[0])

	start_point = (0,0)
	slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
	trees = [
		count_trees(grid, start_point, slope, width, height)
		for slope in slopes
	]

	print("Encountered trees:")
	for s, t in zip(slopes, trees):
		print(s, ":", t, end=", ")

	prod = 1
	for x in trees:
		prod *= x

	print("Product:", prod)

if __name__ == "__main__":
	main()