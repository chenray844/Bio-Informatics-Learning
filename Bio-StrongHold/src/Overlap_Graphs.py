import os
import sys

from Bio import SeqIO

def main(*args, **kwargs):
    in_path = os.path.join(os.getcwd(),args[-2])
    out_path= os.path.join(os.getcwd(),args[-1])
    k = int(args[-3])

    seqs = list(SeqIO.parse(in_path, 'fasta'))
    out_f = open(out_path,'w')

    for value_idx in xrange(len(seqs)):

        for com_value_idx in xrange(len(seqs)):
            if seqs[value_idx].seq.tostring() == seqs[com_value_idx].seq.tostring():
                continue
            if seqs[value_idx].seq.tostring()[:k] == seqs[com_value_idx].seq.tostring()[-k:]:
                txt = " ".join((seqs[com_value_idx].id,seqs[value_idx].id))
                print txt

    out_f.close()

if __name__ == '__main__':
    main(*sys.argv)