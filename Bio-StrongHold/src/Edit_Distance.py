import os
import sys

from Bio import SeqIO
from numpy import zeros

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])

    seqs = list(SeqIO.parse(fpath,'fasta'))
    s = str(seqs[0].seq)
    t = str(seqs[1].seq)

    # Initialize matrix M.
    M = zeros((len(s)+1,len(t)+1), dtype=int)
    for i in xrange(1,len(s)+1):
        M[i][0]= i
    for i in xrange(1,len(t)+1):
        M[0][i]= i

    # Compute each entry of M.
    for i in xrange(1,len(s)+1):
        for j in xrange(1,len(t)+1):
            if s[i-1] == t[j-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j]+1,M[i][j-1]+1, M[i-1][j-1]+1)

    # Print the desired edit distance.
    print M[len(s)][len(t)]

if __name__ == '__main__':
    main(*sys.argv)
