import os
import sys

from Bio import SeqIO
import numpy as np

from StrongHold import Algorithm

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-2])
    dnas = []
    for record in SeqIO.parse(fpath,'fasta'):
        dnas.append(str(record.seq))

    res = np.zeros((len(dnas), len(dnas)), dtype=np.float)

    for i,dna_i in enumerate(dnas):
        for j,dna_j in enumerate(dnas):
            d = Algorithm.pDistance(dna_i, dna_j)
            res[i][j]=d

    for i in xrange(len(dnas)):
        for j in xrange(len(dnas)):
            print res[i][j],
        print

if __name__ == '__main__':
    main(*sys.argv)