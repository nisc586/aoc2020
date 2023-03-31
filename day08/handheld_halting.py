EXAMPLE = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6\
"""

class BootCode:


    def __init__(self, data):
        # Parsing
        instructions = []
        for line in data.splitlines():
            op, _, val = line.partition(" ")
            val = int(val)
            instructions.append((op, val))
        self.__instructions = instructions
        self.reset()


    def reset(self):
        """Resets the instructions list and the accumulator"""
        self.instructions = self.__instructions.copy()
        self.accumulator = 0


    def run(self):
        """Run the program and returns True if successful.

        Returns False if an infinite loop is detected.
        """
        self.accumulator = 0
        pointer = 0
        seen = set()
        while pointer < len(self.instructions):
            # Unpack operation
            operation, value = self.instructions[pointer]

            # Check if the operation already was executed once
            if pointer in seen:
                return False
            else:
                seen.add(pointer)

            # Execute the operation
            if operation == "nop":
                pass
            elif operation == "acc":
                self.accumulator += value
            elif operation == "jmp":
                pointer += value
                continue
            else:
                raise ValueError(f"unknown operation: {operation}")

            pointer += 1
        return True


def test():
    test_bc = BootCode(EXAMPLE)
    exit_code = test_bc.run()
    assert exit_code == False
    assert test_bc.accumulator == 5

    test_bc.instructions[-2] = ("nop", -4)
    exit_code = test_bc.run()
    assert exit_code == True
    assert test_bc.accumulator == 8

def main1():
    with open("day08/input.txt") as f:
        inputs = f.read()
    bc = BootCode(inputs)
    bc.run()
    print("The accumulator holds", bc.accumulator) # expect 5


def main2():
    with open("day08/input.txt") as f:
        inputs = f.read()
    bc = BootCode(inputs)
    i = 0
    remember = tuple()

    while not bc.run():
        # Restore old opcode, if one has been replaced
        if remember:
            bc.reset()
        # Replace nop or jmp with jmp or nop
        op, val = bc.instructions[i]
        if op == "jmp":
            bc.instructions[i] = ("nop", val)
            remember = (i, "jmp")
        elif op == "nop":
            bc.instructions[i] = ("jmp", val)
            remember = (i, "nop")
        i += 1

    print(f"Replaced {remember[1]} in line {remember[0]}.")
    print(f"The accumulator holds {bc.accumulator}.")


if __name__ == "__main__":
    test()
    print("Part1:")
    main1()
    print("Part2:")
    main2()
