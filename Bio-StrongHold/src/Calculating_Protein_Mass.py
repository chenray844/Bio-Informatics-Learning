import os
import sys

from Bio.Seq import Seq
from Bio.Alphabet import generic_protein
from Bio.SeqUtils import molecular_weight

from StrongHold import StrongHold

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])
    s = str(StrongHold.parserDNAFile(fpath))
    mass = molecular_weight(s, seq_type='protein', circular=True, monoisotopic=True)
    print '%.3f' % mass


if __name__ == '__main__':
    main(*sys.argv)