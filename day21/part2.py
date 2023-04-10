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
    
    stack = []
    for allergen, candidates in possible_allergens.items():
        if len(candidates) == 1:
            stack.append(allergen)
    
    while stack:
        allergen = stack.pop()
        solved_food = list(possible_allergens[allergen])[0]
        for key, val in possible_allergens.items():
            if key != allergen:
                if solved_food in val:
                    val.discard(solved_food)
                    if len(val) == 1:
                        stack.append(key)
    
    return ",".join(list(possible_allergens[key])[0] for key in sorted(possible_allergens.keys()))
    

def main():
    with open("day21/input.txt") as f:
        s = f.read()
    print(solve(s))

if __name__ == "__main__":
    assert solve(EXAMPLE) == "mxmxvkd,sqjhc,fvjkl", f"expected: 'mxmxvkd,sqjhc,fvjkl', got: {solve(EXAMPLE)}"
    main()