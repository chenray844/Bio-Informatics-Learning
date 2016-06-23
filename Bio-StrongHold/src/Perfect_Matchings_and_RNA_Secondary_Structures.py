from collections import Counter
from math import factorial
from Bio import SeqIO

import os
import sys

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])
    seq = str(SeqIO.read(fpath,'fasta').seq)

    counts = Counter(seq)

    pn = factorial(counts['A'])*factorial(counts['C'])

    print pn

if __name__ == '__main__':
    main(*sys.argv)