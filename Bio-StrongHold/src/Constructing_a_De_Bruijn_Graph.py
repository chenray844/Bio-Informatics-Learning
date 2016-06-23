import os
import sys

from Bio.Seq import Seq

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-2])
    tmp = []
    with open(fpath,'r') as f:
        for line in f:
            txt = line.strip()
            tmp.append(txt)

    S1 = set(tmp)
    S2 = set([str(Seq(s).reverse_complement()) for s in tmp])

    S = S1.union(S2)

    res = []
    for s in S:
        res.append((s[:-1],s[1:]))

    for t1,t2 in res:
        print '(%s, %s)' % (t1,t2)

    out = os.path.join(os.getcwd(),args[-1])
    f = open(out, 'w')
    for t1,t2 in res:
        txt = '(%s, %s)\n' % (t1,t2)
        f.write(txt)
    f.close()

if __name__ == '__main__':
    main(*sys.argv)
