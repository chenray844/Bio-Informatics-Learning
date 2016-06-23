import os
import sys

from Bio import SeqIO
from Bio.Seq import Seq

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])

    records = list(SeqIO.parse(fpath,'fasta'))
    s = str(records[0].seq)
    t = str(records[1].seq)

    idxs = []
    idx = 0
    for m in t:
        idx = s.find(m,idx)

        idx += 1
        idxs.append(idx)

    for idx in idxs:
        print idx,

if __name__ == '__main__':
    main(*sys.argv)

