EXAMPLE = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

class CombatGame:
    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2
    
    def round(self):
        assert self.deck1 and self.deck2

        card1 = self.deck1.pop()
        card2 = self.deck2.pop()

        pl1_wins = card1 > card2
        if pl1_wins:
            self.deck1.insert(0, card1)
            self.deck1.insert(0, card2)
        else:
            self.deck2.insert(0, card2)
            self.deck2.insert(0, card1)
    
    def run(self):
        while self.deck1 and self.deck2:
            self.round()
    
    def score_calc(self):
        if self.deck1:
            return sum(val * (i+1) for i, val in enumerate(self.deck1))
        else:
            return sum(val * (i+1) for i, val in enumerate(self.deck2))


def parse(s):
    deck1_s, deck2_s = s.split("\n\n")
    deck1 = [int(line) for line in deck1_s.splitlines()[1:]]
    deck2 = [int(line) for line in deck2_s.splitlines()[1:]]

    deck1.reverse()
    deck2.reverse()
    return deck1, deck2

def solve(s):
    deck1, deck2 = parse(s)
    game = CombatGame(deck1, deck2)
    game.run()
    return game.score_calc()

def test():
    assert solve(EXAMPLE) == 306

def main():
    with open("day22/input.txt") as f:
        s = f.read()
    print(solve(s))

if __name__ == "__main__":
    test()
    main()