from math import factorial

n = 86
k = 8

res = factorial(n)/factorial(n-k)%1e6
print int(res)
