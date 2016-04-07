import sys
import os

from Bio import SeqIO

#
# for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
#     print(seq_record.id)
#     print(repr(seq_record.seq))
#     print(len(seq_record))

def main(*args, **kwargs):
    curPath = os.getcwd()
    filename = os.path.join(curPath, 'data','ls_orchid.fasta')
    for seq_record in SeqIO.parse(str(filename),'fasta'):
        print seq_record.id
        print repr(seq_record.seq)
        print len(seq_record)


if __name__ == '__main__':
    main(sys.argv)