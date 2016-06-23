def get_bin(n, p):
    frequencies = []

    for j in p:
        frequencies.append(n * float(j))

    return frequencies

if __name__ == '__main__':
    dataset = open('data/data.dat')

    n = int(dataset.readline())
    p = dataset.readline().split()

print ' '.join(str(x) for x in get_bin(n, p))