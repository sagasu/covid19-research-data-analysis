import random
import numpy as np
""" 
This is a gamblers dilemma problem
we have 10 pounds, and we toss a coin, each time we toss head we gain 1 pound, else we loose 1 pound
we are checking if we run out of money, and when
"""

def get_count_before_run_out_of_money():
    money, count = 10, 0
    while money:
        toss = random.random()
        if toss < .50:
            money -= 1
        if toss > .50:
            money += 1
        count += 1
    return count

sims = [get_count_before_run_out_of_money() for _ in range(100)]

print(np.mean(sims))
print(np.percentile(sims, np.arange(0, 100, 10)))
print(sims)