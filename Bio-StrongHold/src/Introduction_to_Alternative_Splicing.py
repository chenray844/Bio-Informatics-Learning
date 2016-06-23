from scipy.misc import comb

n = 1950

m = 1116

res = []

for k in xrange(m,n+1):
    value = comb(n,k,exact=True)
    res.append(value)

res = sum(res)%int(1e6)

print res
