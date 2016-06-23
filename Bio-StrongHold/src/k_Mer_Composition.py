from Bio import SeqIO
from itertools import product
import re

import os
import sys

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-2])
    dna = str(SeqIO.read(fpath,'fasta').seq)

    perms = product(['A','C','G','T'], repeat=4)
    kmers = []
    for perm in perms:
        kmers.append(''.join(perm))

    opath = os.path.join(os.getcwd(),args[-1])
    fo = open(opath, 'w')
    for kmer in kmers:
        txt = '%s\t' % len(re.findall(''.join(['(?=', kmer, ')']), dna))
        fo.write(txt)
    fo.close()

if __name__ == '__main__':
    main(*sys.argv)