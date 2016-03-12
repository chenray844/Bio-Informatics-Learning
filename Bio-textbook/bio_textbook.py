import sys

def prog_01(fname):
    f = open(fname)

    hmm = None
    stats = None
    pstats = {}
    for i,line in enumerate(f):
        if i == 0:
            hmm = line.strip()
        if i == 2:
            stats = line.strip().split()
            print stats
        if i == 4:
            idxs1 = line.strip().split()
        if i == 5:
            strs = line.strip().split()
            pstats[strs[0]+'-'+idxs1[0]] = eval(strs[1])
            pstats[strs[0]+'-'+idxs1[1]] = eval(strs[2])
        if i == 6:
            strs = line.strip().split()
            pstats[strs[0]+'-'+idxs1[0]] = eval(strs[1])
            pstats[strs[0]+'-'+idxs1[1]] = eval(strs[2])

    print hmm,pstats,stats
    # aa = 0.194
    # ab = 0.806
    # ba = 0.273
    # bb = 0.727
    # pi = (aa,ab,ba,bb)
    # p = 1
    # s1 =None
    # s2 = None
    # for i,s in enumerate(hmm):
    #     if i==0:
    #         s1 = s
    #         p *= 0.5
    #         continue
    #     s2 = s
    #     if s1==s2:
    #         if s1=='A':
    #             p *= pi[0]
    #         if s1=='B':
    #             p *= pi[3]
    #     else:
    #         if s1=='A' and s2 =="B":
    #             p *= pi[1]
    #         if s1=="B" and s2 =="A":
    #             p *= pi[2]
    #     s1 = s

    f.close()

    p = 1

    s1, s2 = None, None

    for i,s in enumerate(hmm):
        if i == 0:
            s1 = s
            p *= 0.5
            continue

        s2 = s
        k = '%s-%s' % (s1,s2)
        p *= pstats[k]
        s1 = s

    print p

if __name__ == '__main__':
    args = sys.argv
    if args[1] == '-01':
        prog_01(args[2])