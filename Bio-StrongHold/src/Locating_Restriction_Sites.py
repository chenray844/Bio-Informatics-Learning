import os
import sys

from Bio import SeqIO
from Bio.Seq import Seq

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])
    seq = SeqIO.read(fpath,'fasta')
    seq = str(seq.seq)
    print seq,len(seq)
    for start,s in enumerate(seq):
        for num in xrange(4,12+1):
            end = start + num
            if end>len(seq):
                break
            if str(seq[start:end])==str(Seq(seq[start:end]).reverse_complement()):
                print start+1,num

if __name__ == '__main__':
    main(*sys.argv)