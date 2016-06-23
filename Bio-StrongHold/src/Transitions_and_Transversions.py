import os
import sys

from Bio import SeqIO
from Bio.Seq import Seq

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])

    records = list(SeqIO.parse(fpath, 'fasta'))
    seq1 = str(records[0].seq)
    seq2 = str(records[1].seq)

    transitions = 0
    transversions = 0
    for i,s1 in enumerate(seq1):
        s2 = seq2[i]
        if (s1 == "A" and s2 == 'G') or (s1 == 'G' and s2 == 'A'):
            transitions += 1
        elif (s1 == 'C' and s2 == 'T') or (s1 == 'T' and s2 == 'C'):
            transitions += 1
        elif s1 == s2:
            continue
        else:
            transversions +=1

    print float(transitions)/float(transversions)

if __name__ == '__main__':
    main(*sys.argv)
