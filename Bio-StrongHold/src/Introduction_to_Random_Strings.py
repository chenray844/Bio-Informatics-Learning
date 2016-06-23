import os
import sys
from math import log10

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-2])
    f = open(fpath, 'r')
    seq = f.readline().strip()
    gc_array = map(float, f.readline().strip().split())
    f.close()

    opath = os.path.join(os.getcwd(), args[-1])
    fo = open(opath, 'w')
    for gc in gc_array:
        prob_gc = gc/2
        prob_at = (1-gc)/2

        prob = 1
        for gen in seq:
            if gen == 'A' or gen == 'T':
                prob *=prob_at
            else:
                prob *=prob_gc
        txt = "%.3f\t" % log10(prob)
        fo.write(txt)
    fo.close()

if __name__ == '__main__':
    main(*sys.argv)
