import os
import sys

from Bio import SeqIO, motifs
from Bio.Seq import Seq


def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])
    instances = list()
    for record in SeqIO.parse(str(fpath),'fasta'):
        instances.append(record.seq)
    m = motifs.create(instances)

    consensus = m.consensus
    print consensus

    profile = m.counts
    print 'A:',
    for elem in profile['A']:
        print elem,

    print '\nC:',
    for elem in profile['C']:
        print elem,

    print '\nG:',
    for elem in profile['G']:
        print elem,

    print '\nT:',
    for elem in profile['T']:
        print elem,

if __name__ == '__main__':
    main(*sys.argv)