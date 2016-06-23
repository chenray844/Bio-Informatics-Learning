import os
import sys

from Bio.Seq import Seq

from StrongHold import StrongHold, Algorithm

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])
    s,t = StrongHold.two_dna(fpath)
    s,t = Seq(s),Seq(t)
    idx = 0
    start=0

    while idx!=-1:
        idx = s.find(t, start=start)
        start = idx+1
        if idx!=-1:
            print idx+1,

if __name__ == '__main__':
    main(*sys.argv)