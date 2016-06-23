import os
import sys

from Bio import SeqIO
from StrongHold import Algorithm

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])

    rna = str(SeqIO.read(fpath,'fasta').seq)
    res = Algorithm.catalan_number(rna, 0, len(rna)-1, {})
    print int(res % 1e6)


if __name__ == '__main__':
    main(*sys.argv)