from itertools import product

n = 6

n1 = [i for i in range(1,n+1)] + [-1*i for i in xrange(1,n+1)]

res = list()
for prod in product(n1,repeat=n):
    check = set([abs(v) for v in prod])
    if len(check)==n:
        res.append(prod)
print len(res)
for r in res:
    for v in r:
        print v,
    print

fo = open('out.dat','w')
fo.write("%s\n" % len(res))
for r in res:
    for v in r:
        fo.write("%s\t" % v)
    fo.write("\n")

fo.close()