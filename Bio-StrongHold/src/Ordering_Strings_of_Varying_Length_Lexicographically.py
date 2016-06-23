import os
import sys

from itertools import product

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-2])
    f = open(fpath)
    strs = f.readline().strip().split()
    n = int(f.readline().strip())
    f.close()

    perms = []
    for perm in product(strs, repeat=n):
        for i in xrange(1,n+1):
            if perm[:i] not in perms:
                perms.append(perm[:i])

    out = os.path.join(os.getcwd(), args[-1])
    f = open(out, 'w')
    for perm in perms:
        txt = ''.join(perm)+'\n'
        f.write(txt)
    f.close()

if __name__ == '__main__':
    main(*sys.argv)


