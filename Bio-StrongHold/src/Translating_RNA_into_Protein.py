import sys
import os

from Bio.Seq import Seq
from StrongHold import StrongHold

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])
    SH = StrongHold()
    rna = SH.parserDNAFile(fpath)

    seq = Seq(str(rna))

    protein = seq.translate()
    print protein

if __name__ == '__main__':
    main(*sys.argv)