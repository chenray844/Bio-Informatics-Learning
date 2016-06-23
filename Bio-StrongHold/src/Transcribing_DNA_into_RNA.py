import sys
import os

from Bio.Seq import Seq
from StrongHold import StrongHold

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])
    SH = StrongHold()
    dna = SH.parserDNAFile(fpath)

    seq = Seq(str(dna))

    rna = seq.transcribe()
    print rna

if __name__ == '__main__':
    main(*sys.argv)