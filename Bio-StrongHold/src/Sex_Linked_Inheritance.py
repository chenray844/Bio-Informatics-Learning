# B = [2*(x - x**2) for x in A]

if __name__ == '__main__':
    A = None
    with open('data/data.dat') as f:
        line = f.readline().strip()
        A = map(float, line.split())


    B = None
    if A:
        B = [2*(x-x**2) for x in A]

    if B:
        print ' '.join(map(str, B))
    else:
        print 'Error'
