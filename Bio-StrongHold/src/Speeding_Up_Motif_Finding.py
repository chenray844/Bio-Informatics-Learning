import os
import sys

from Bio import SeqIO
from StrongHold import Algorithm

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-2])
    seq = str(SeqIO.read(fpath, 'fasta').seq)

    arr = Algorithm.KMP_failure_table(seq)

    out = os.path.join(os.getcwd(), args[-1])

    with open(out, 'w') as f:
        txt = ' '.join(map(str,arr))
        f.write(txt)

if __name__ == '__main__':
    main(*sys.argv)