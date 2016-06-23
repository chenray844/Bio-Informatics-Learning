import os
import sys

from Bio import SeqIO

from StrongHold import Algorithm

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])

    seqs = list(SeqIO.parse(fpath, 'fasta'))

    seq1 = str(seqs[0].seq)
    seq2 = str(seqs[1].seq)

    res = Algorithm.longest_common_subsequence(seq1, seq2)
    print res


if __name__ == '__main__':
    main(*sys.argv)