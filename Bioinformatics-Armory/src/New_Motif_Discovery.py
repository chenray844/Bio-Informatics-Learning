import sys
import os

from Bio import SeqIO

def main(fname):
    records = list(SeqIO.parse(fname,'fasta'))
    print records

if __name__ == '__main__':
    fname = os.path.join(os.getcwd(), sys.argv[-1])
    main(fname)