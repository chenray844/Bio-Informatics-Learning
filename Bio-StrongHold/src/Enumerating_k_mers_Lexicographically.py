from itertools import product

import os
import sys

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-2])
    out = os.path.join(os.getcwd(),args[-1])

    f = open(fpath,'r')
    alphabets = str(f.readline()).strip().split()
    n = eval(f.readline())
    f.close()

    fo = open(out,'w')
    for perm in product(alphabets, repeat=n):
        txt = ''.join(perm)+'\n'
        fo.write(txt)

    fo.close()

if __name__ == '__main__':
    main(*sys.argv)