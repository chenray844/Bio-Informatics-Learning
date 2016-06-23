import os
import sys

from collections import Counter
from Bio import SeqIO

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-2])

    seqs = []
    orig_seqs = []
    for s in SeqIO.parse(fpath, 'fasta'):
        orig_seqs.append(str(s.seq))
        seqs.append(str(s.seq))
        seqs.append(str(s.seq.reverse_complement()))

    counts = Counter(seqs)

    def correct_incorrect(counts, orig_seqs):
        correct = []
        incorrect=[]
        for s in counts:
            if counts[s] >= 2:
                correct.append(s)
            elif s in orig_seqs:
                incorrect.append(s)
        return correct,incorrect

    def hamming(seq1, seq2):
        mutations = 0
        for i,s1 in enumerate(seq1):
            s2 = seq2[i]
            if s1 != s2:
                mutations += 1
        return mutations

    def corrections(correct, incorrect):
        corrected = []
        for seq1 in incorrect:
            for seq2 in correct:
                if hamming(seq1, seq2) == 1:
                    corrected.append((seq1, seq2))
        return corrected

    correct, incorrect = correct_incorrect(counts, orig_seqs)
    corrs = corrections(correct, incorrect)

    opath = os.path.join(os.getcwd(), args[-1])
    fo = open(opath, 'w')
    for ss in corrs:
        txt = '->'.join(ss)+'\n'
        fo.write(txt)
    fo.close()


if __name__ == '__main__':
    main(*sys.argv)
