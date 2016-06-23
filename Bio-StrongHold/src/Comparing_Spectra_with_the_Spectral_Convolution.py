import os
import sys

def main(*args,**kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])
    f = open(fpath,'r')
    S1 = map(float, f.readline().strip().split())
    S2 = map(float, f.readline().strip().split())
    f.close()

    spectral_convolution = {}
    for s1 in S1:
        for s2 in S2:
            element = str(s1-s2)
            if element in spectral_convolution:
                spectral_convolution[element] += 1
            else:
                spectral_convolution[element] = 1

    max_multiplicty = max(spectral_convolution.values())

    max_elem = [elem for elem, count in spectral_convolution.iteritems() if count == max_multiplicty]

    print max_multiplicty
    print max_elem[0]

if __name__ == '__main__':
    main(*sys.argv)