import os
import sys

from Bio import SeqIO
from math import factorial

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])
    rna = str(SeqIO.read(fpath, 'fasta').seq)

    AU,GC = [],[]
    for v in 'AU':
        AU.append(rna.count(v))
    for v in 'GC':
        GC.append(rna.count(v))

    print factorial(max(AU))/factorial(max(AU)-min(AU))*factorial(max(GC))/factorial(max(GC)-min(GC))

if __name__ == '__main__':
    main(*sys.argv)