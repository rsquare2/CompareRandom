# NumberSelect.py

"""for each number 1-10 pick random number ("pick") and see if there is a match
     if there is a match increase "match" by one
     divide total matches over specified number of rounds and divide by total rounds
"""

import random

def compare(rounds):
    match = 0


    for round in range(rounds):
        for counter in range(1,11):
            pick = random.randint(1,10)
            if counter == pick:
                match += 1
                # print("****Match: ",counter, pick)

            # else:
                # print("No Match: ", counter, pick)

    print("Total Matches: ",match)
    print("Rounds: ", rounds)
    print("Avg Matches Per Round: ", (match/rounds))

compare(20000)