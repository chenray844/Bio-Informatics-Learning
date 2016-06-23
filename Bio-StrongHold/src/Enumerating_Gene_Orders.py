from itertools import permutations
from math import factorial

n = 5
seq = range(1, n+1)

print factorial(n)

for perm in permutations(seq):
    print " ".join(map(str, perm))
