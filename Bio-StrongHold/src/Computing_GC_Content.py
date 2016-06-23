import sys
import os

from Bio import SeqIO,Seq

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])

    dict_record = SeqIO.to_dict(SeqIO.parse(str(fpath),'fasta'))
    for id, record in dict_record.iteritems():
        seq = record.seq
        seq = Seq.Seq(str(seq))
        print id, float(seq.count('G')+seq.count('C'))/float(len(seq))*100.0


if __name__ == '__main__':
    main(*sys.argv)