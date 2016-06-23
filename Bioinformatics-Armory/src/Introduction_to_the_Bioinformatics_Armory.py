import sys
import os

from Bio.Seq import Seq

def main(fname):
    dna = None
    with open(fname) as f:
        dna = f.read().strip()

    seq = Seq(dna)

    for item in ['A','C','G', 'T']:
        print seq.count(item),

if __name__ == '__main__':
    fname = sys.argv[1]
    fname = os.path.join(os.getcwd(), fname)
    main(fname)