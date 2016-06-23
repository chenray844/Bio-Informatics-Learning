import os
import sys

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])
    f = open(fpath, 'r')
    n = int(f.readline().strip())
    dna = f.readline().strip()
    A = map(float, f.readline().strip().split())
    f.close()

    counts = {'GC':dna.count("G")+dna.count('C'),
              'AT':dna.count('A')+dna.count('T'),
              }
    substr_len = n - len(dna) + 1

    res = []
    for i, prob_gc in enumerate(A):
        prob = ((0.5*prob_gc)**counts['GC']) * ((0.5*(1-prob_gc))**counts['AT'])
        res.append(prob*substr_len)

    txt = ' '.join(map(str,res))
    print txt

if __name__ == '__main__':
    main(*sys.argv)