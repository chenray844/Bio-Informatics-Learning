import os
import sys

def format(S):

    txt = ', '.join(map(str,S))
    txt = '{'+txt+'}'
    return txt

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])
    f = open(fpath,'r')
    n = int(f.readline().strip())
    A = map(int, str(f.readline().strip())[1:-1].split(','))
    B = map(int, str(f.readline().strip())[1:-1].split(','))
    f.close()

    U = set(range(1,n+1))
    A = set(A)
    B = set(B)

    print format(A.union(B))
    print format(A.intersection(B))
    print format(A.difference(B))
    print format(B.difference(A))
    print format(U.difference(A))
    print format(U.difference(B))



if __name__ =="__main__":
    main(*sys.argv)