import os
import sys

from StrongHold import StrongHold, Algorithm

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])
    s1,s2 = StrongHold.two_dna(fpath)
    print Algorithm.hammingDistance(s1,s2)

if __name__ == '__main__':
    main(*sys.argv)