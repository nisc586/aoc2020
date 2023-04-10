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

class RecursiveCombatGame:
    def __init__(self, deck1, deck2):
        self.deck1 = tuple(deck1)
        self.deck2 = tuple(deck2)
        self.configurations = set()
        self.pl1_wins = False
    
    def round(self):
        # Condition 1: no previous round with the same configuration
        state = (self.deck1, self.deck2)
        if (state in self.configurations):
            self.deck1 += self.deck2
            self.deck2 = ()
            self.pl1_wins = True
            return
        else:
            self.configurations.add(state)

        card1, *rest1 = self.deck1
        card2, *rest2 = self.deck2

        # Condition 2: the game recurses
        if ((card1 <= len(rest1)) and (card2 <= len(rest2))):
            
            subgame = RecursiveCombatGame(rest1[:card1], rest2[:card2])
            subgame.run()
            self.pl1_wins = subgame.pl1_wins
        else:
            self.pl1_wins = card1 > card2

        if self.pl1_wins:
            self.deck1 = tuple(rest1) + (card1, card2)
            self.deck2 = tuple(rest2)
        else:
            self.deck2 = tuple(rest2) + (card2, card1)
            self.deck1 = tuple(rest1)
    
    def run(self):
        while self.deck1 and self.deck2:
            self.round()
    
    def score_calc(self):
        if self.deck1:
            return sum(val * (i+1) for i, val in enumerate(reversed(self.deck1)))
        else:
            return sum(val * (i+1) for i, val in enumerate(reversed(self.deck2)))


def parse(s):
    deck1_s, deck2_s = s.split("\n\n")
    deck1 = [int(line) for line in deck1_s.splitlines()[1:]]
    deck2 = [int(line) for line in deck2_s.splitlines()[1:]]

    return deck1, deck2

def solve(s):
    deck1, deck2 = parse(s)
    game = RecursiveCombatGame(deck1, deck2)
    game.run()
    return game.score_calc()

def test():
    assert solve(EXAMPLE) == 291

def test_no_infinite_game():
    S = """Player 1:
43
19

Player 2:
2
29
14"""
    deck1, deck2 = parse(S)
    game = RecursiveCombatGame(deck1, deck2)
    print("Test start...")
    game.run()
    print("Test stop!")

def main():
    with open("day22/input.txt") as f:
        s = f.read()
    print(solve(s))

if __name__ == "__main__":
    test_no_infinite_game()
    test()
    main()