import os
import sys

from Bio import SeqIO

from StrongHold import Algorithm

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])
    rna = str(SeqIO.read(fpath,'fasta').seq)

    noncorss_dict = {}
    noncorss = Algorithm.Motzkin_Numbers(rna, noncorss_dict)
    print noncorss


if __name__ == '__main__':
    main(*sys.argv)