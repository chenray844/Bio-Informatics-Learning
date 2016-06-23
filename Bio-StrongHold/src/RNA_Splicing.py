import os
import sys

from Bio.Seq import Seq
from Bio import SeqIO

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])
    dna = None
    introns = list()
    for i,record in enumerate(SeqIO.parse(fpath,'fasta')):
        if i==0:
            dna = str(record.seq)
            continue
        introns.append(str(record.seq))

    for intron in introns:
        if intron in dna:
            dna = dna.replace(intron,'')

    print Seq(str(dna)).translate(to_stop=True)

if __name__ == '__main__':
    main(*sys.argv)