import os
import sys

from random import random

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])
    f = open(fpath)
    n,prob_gc = map(float, f.readline().strip().split())
    dna = str(f.readline().strip())
    f.close()

    prob_at = 1-prob_gc

    prob = 1
    for nucleotide in dna:
        if nucleotide in ['A','T']:
            prob *= prob_at/2
        elif nucleotide in ['C', 'G']:
            prob *= prob_gc/2

    print 1-(1-prob)**n

if __name__ == '__main__':
    main(*sys.argv)