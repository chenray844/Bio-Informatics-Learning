from Bio import SeqIO

def maximum_gap_symbols(v, w):
    '''Returns the max number of gap symbols in an optimal alignment of v and w.'''
    # Get the length of the longest common subsequence.
    M = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    for i in xrange(len(v)):
        for j in xrange(len(w)):
            if v[i] == w[j]:
                M[i+1][j+1] = M[i][j]+1
            else:
                M[i+1][j+1] = max(M[i+1][j],M[i][j+1])

    # Apply the aforementioned formula with the length of the longest subsequence.
    return len(v) + len(w) - 2*M[len(v)][len(w)]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Parse the input data.
    v, w = list(SeqIO.parse('data/fasta.fasta','fasta'))

    v = str(v)
    w = str(w)

    # Get the maximum number of gaps.
    max_gaps = str(maximum_gap_symbols(v,w))

    # Print and save the answer.
    print max_gaps


if __name__ == '__main__':
    main()