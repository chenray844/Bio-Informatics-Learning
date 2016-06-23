import os
import sys

from Bio import SeqIO

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])
    raw_data = list(SeqIO.parse(fpath, 'fasta'))

    sequences = []
    for seq in raw_data:
        sequences.append(str(seq.seq))

    lengths = map(len, sequences)
    index = lengths.index(min(lengths))
    shortest_sequence = sequences[index]

    lcs = ''
    for start in xrange(len(shortest_sequence)):
        for end in xrange(len(shortest_sequence), start, -1):
            if len(shortest_sequence[start:end]) > len(lcs):
                   matches = []
                   for seq in sequences:
                       if shortest_sequence[start:end] in seq:
                           matches.append(True)
                       else:
                           matches.append(False)
                           break
                   if all(matches):
                       lcs = shortest_sequence[start:end]
                       break
            else:
                   break

    print lcs

if __name__ == '__main__':
    main(*sys.argv)