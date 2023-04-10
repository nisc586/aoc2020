import re
from collections import defaultdict, Counter

EXAMPLE = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

def parse(s):
    pattern = r"^([a-z ]+) \(contains ([a-z, ]+)\)$"
    result = []
    for line in s.splitlines():
        m = re.match(pattern, line)
        foods = m.group(1).split(" ")
        allergens = m.group(2).split(", ")
        result.append((foods, allergens))
    return result


def solve(s):
    foodlist = parse(s)
    all_foods = set.union(*[set(food) for food, _ in foodlist])
    possible_allergens = defaultdict(lambda: all_foods.copy())

    for fds, algs in foodlist:
        for allergen in algs:
            possible_allergens[allergen] &= set(fds)
    
    save_foods = all_foods.difference(*[set(fds) for fds in possible_allergens.values()])
    
    count = Counter(
        food
        for fds, _ in foodlist
        for food in fds
        if food in save_foods
    )
    return count.total()
    

def main():
    with open("day21/input.txt") as f:
        s = f.read()
    print(solve(s))

if __name__ == "__main__":
    assert solve(EXAMPLE) == 5, f"expected: 5, got: {solve(EXAMPLE)}"
    main()