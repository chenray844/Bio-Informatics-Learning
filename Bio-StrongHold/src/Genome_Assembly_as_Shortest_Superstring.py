from Bio import SeqIO
import pandas as pd

import os
import sys
import time

def assemble(seqs):
    # matrix of overlap lengths
    overlaps = getAllOverlaps(seqs)
    # list of reads in order of alignment
    seq_order = findOrder(overlaps)

    final_sequence = str(seqs[seq_order[0]].seq)
    for index in xrange(1, len(seq_order)):
        # find length of overlap
        over_len = int(overlaps[seq_order[index-1]][seq_order[index]])
        # remove overlap from first sequence and append next
        final_sequence = final_sequence[:-over_len] + str(seqs[seq_order[index]].seq)
    return final_sequence

def findOrder(overlaps):
    seq_order = [findStartRead(overlaps)]
    for seq in xrange(overlaps.shape[1]-1): #pd.shape returns dimensions of matrix
        seq_order.append(findLargestOverlap(seq_order[seq], overlaps))
    return seq_order

def findLargestOverlap(key, overlaps):
    # idxmax returns key (i.e. column name) of highest value (i.e. length of overlap)
    return overlaps[key].idxmax()

def findStartRead(overlaps):
    # the read with the lowest amount of overlap to the left will be the first read
    # add values and see which read had the lowest overlapping
    # idxmin returns key
    return overlaps.sum(axis=1, skipna=True).idxmin()

# Create dictionary of dictionaries of all overlap comparisons
def getAllOverlaps(reads):
    overlap_counts = {}
    for first_key, first_value in reads.iteritems():
        inner_dict = {}
        for second_key, second_value in reads.iteritems():
            if first_key == second_key:
                inner_dict[second_key] = 'NA'
            else:
                inner_dict[second_key] = getOverlap(first_value, second_value)
        overlap_counts[first_key] = inner_dict
    # to make the nested dictionaries more accessible (and pretty!) convert to pandas dataframe
    # minor issue - probably should make sure type is integer instead of float
    return pd.DataFrame(overlap_counts).convert_objects(convert_numeric=True)

''' since assuming no errors and no nested pairings, then only
    overlaps over a prefix and suffix of two strings '''
def getOverlap(first, second):
    # take prefix of second and compare to suffix of first
    nt = 3 # how many nucleotides must match at least, arbitrary for these purposes
    index = ''
    first = str(first.seq)
    second = str(second.seq)
    finish = False
    while finish == False:
        # keep extending length until no overlap
        if second[:nt] == first[-nt:]:
            index = second[:nt]
            nt += 1
        # check if the prefix is even in the other sequence/read
        elif second[:nt] in first[1:]:
            nt += 1
        else:
            finish = True
    return len(index)

# second
def find_overlaps(arr, acc=''):
    if len(arr) == 0:
        return acc

    elif len(acc) == 0:
        acc = arr.pop(0)
        return find_overlaps(arr, acc)

    else:

        for i in range(len(arr)):
            a = arr[i]
            l = len(a)

            for p in range(l / 2):
                q = l - p

                if acc.startswith(a[p:]):
                    arr.pop(i)
                    return find_overlaps(arr, a[:p] + acc)

                if acc.endswith(a[:q]):
                    arr.pop(i)
                    return find_overlaps(arr, acc + a[q:])

from StrongHold import Algorithm

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])
    record_dict = SeqIO.to_dict(SeqIO.parse(fpath,'fasta'))
    print assemble(record_dict)

    print '\n\n\n'

    t1 = time.time()
    res = find_overlaps(map(str,[seq.seq for seq in record_dict.values()]))
    print res
    t2 = time.time()
    print '\n\n',t2-t1,'ms'

    print '\n\n\n'
    print Algorithm.find_shortest_superstring(map(str, [seq.seq for seq in record_dict.values()]))

if __name__ == '__main__':
    main(*sys.argv)