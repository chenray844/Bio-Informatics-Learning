import os
import sys

def longest_increasing_subsequence(d):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len)
                  + [d[i]])
    return max(l, key=len)

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])
    f = open(fpath,'r')
    n = eval(f.readline())
    d = map(int, f.readline().strip().split())
    lis = longest_increasing_subsequence(d)
    print ' '.join(map(str,lis))
    dd = [-1*v for v in d]
    # print d
    lds = longest_increasing_subsequence(dd)
    print ' '.join(map(str,map(lambda x:-1*x,lds)))

if __name__ == '__main__':
    main(*sys.argv)