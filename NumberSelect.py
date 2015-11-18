# NumberSelect.py

"""for each number 1-10 pick random number ("pick") and see if there is a match
     if there is a match increase "match" by one
     divide total matches over specified number of rounds and divide by total rounds
"""

import random

class Compare:

    def __init__(self,rounds):
        self.rounds = rounds
        self.match = 0


    def selectRandom(self):
        for round in range(self.rounds):
            for counter in range(1,11):
                pick = random.randint(1,10)
                if counter == pick:
                    self.match += 1

        print("Total Matches: ",self.match)
        print("Rounds: ", self.rounds)
        print("Avg Matches Per Round: ", (self.match/self.rounds))

def main():
    a = Compare(10000)
    b = a.selectRandom()

if __name__ == '__main__': main()
