import os
import sys

from StrongHold import MONOISOTOPIC_MASS_TABLE

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])
    prefix_spectrum = []
    with open(fpath,'r') as f:
        for line in f:
            prefix_spectrum.append(eval(line.strip()))

    inverted_table = {}
    for k,v in MONOISOTOPIC_MASS_TABLE.iteritems():
        inverted_table[round(v, 4)] = k

    result = ''
    for i in xrange(1, len(prefix_spectrum)):
        a = prefix_spectrum[i-1]
        b = prefix_spectrum[i]
        result += inverted_table[round(b-a, 4)]
    return result


if __name__ == "__main__":

    res = main(*sys.argv)
    print res