def Nxx(dna, xx):
    # Create a list containing n copies of an integer, n; where n is the
    # length of each given string in a list.
    lenlist = []
    for i in dna:
        lenlist += [len(i)]*len(i)
    lenlist = sorted(lenlist)

    # Take the mean of the two middle elements if there are an even number
    # of elements. Otherwise, take the middle element.
    n = 100 / (100 - xx)
    if len(lenlist) % 2 == 0:
        medianpos = int(len(lenlist) / n)
        return lenlist[medianpos] + lenlist[medianpos-1] / n
    else:
        medianpos = int(len(lenlist) / n)
        return lenlist[medianpos]


def main():
    with open('data/data.dat', 'r') as infile:
        dna = infile.read().strip().split('\n')

    print ' '.join(map(str,[Nxx(dna, 50), Nxx(dna, 75)]))


if __name__ == '__main__':
    main()