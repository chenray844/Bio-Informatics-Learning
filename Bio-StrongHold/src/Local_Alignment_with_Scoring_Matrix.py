from Bio.SubsMat.MatrixInfo import pam250
from Bio import SeqIO
from Bio.Seq import Seq

def local_alignment(v, w, scoring_matrix, sigma):
    '''Returns the score and local alignment with the given scoring matrix and indel penalty sigma for strings v, w.'''
    from numpy import unravel_index, zeros

    # Initialize the matrices.
    S = zeros((len(v)+1, len(w)+1), dtype=int)
    backtrack = zeros((len(v)+1, len(w)+1), dtype=int)

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            try:
                scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]], 0]
            except:
                scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoring_matrix[w[j-1], v[i-1]], 0]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    # Get the position of the highest scoring cell in the matrix and the high score.
    i,j = unravel_index(S.argmax(), S.shape)
    max_score = str(S[i][j])

    # Initialize the aligned strings as the input strings up to the position of the high score.
    v_aligned, w_aligned = v[:i], w[:j]

    # Backtrack to start of the local alignment starting at the highest scoring cell.
    while backtrack[i][j] != 3 and i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
        elif backtrack[i][j] == 1:
            j -= 1
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    # Cut the strings at the ending point of the backtrack.
    v_aligned = v_aligned[i:]
    w_aligned = w_aligned[j:]

    return max_score, str(v_aligned.seq), str(w_aligned.seq)

if __name__ == '__main__':

   # Parse the two input protein strings.
    s, t = list(SeqIO.parse('data/fasta.fasta','fasta'))

    # Get the local alignment (given sigma = 5 in problem statement).
    alignment = local_alignment(s, t, pam250, 5)

    # Print and save the answer.
    print '\n'.join(alignment)