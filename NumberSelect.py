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
        self.maxMatchesSoFar = 0
        self.match1 = 0
        self.match2 = 0
        self.match3 = 0
        

    def selectRandom(self):
        for round in range(self.rounds):
            self.maxMatches = 0
            for counter in range(1,11):
                pick = random.randint(1,10)
                if counter == pick:
                    self.match += 1
                    self.maxMatches +=1
                            
                if self.maxMatches > self.maxMatchesSoFar:
                    self.maxMatchesSoFar = self.maxMatches

            if self.maxMatches == 1:
                   self.match1 += 1
            if self.maxMatches == 2:
                   self.match2 += 1
            if self.maxMatches == 3:
                   self.match3 += 1
 

        print("Total Matches: ",self.match)
        print("Rounds: ", self.rounds)
        print("Avg Matches Per Round: ", (self.match/self.rounds))
        print("Max Matches in a Round: ", self.maxMatchesSoFar)
        print("1 Match Rounds: {0}%".format(int((self.match1/self.rounds)*100)))
        print("2 Match Rounds: {0}%".format(int((self.match2/self.rounds)*100)))
        print("3 Match Rounds: {0}%".format(int((self.match3/self.rounds)*100)))
                
def main():
    a = Compare(100000)
    b = a.selectRandom()

if __name__ == '__main__': main()
