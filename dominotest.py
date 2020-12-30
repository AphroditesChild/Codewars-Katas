from itertools import combinations, permutations
from random import random, randint, choice, sample

ALL_PIECES = sorted(list(combinations(range(7), 2))+[(i,i) for i in range(7)])

print(ALL_PIECES)
print(sample(ALL_PIECES, 7))

input()
