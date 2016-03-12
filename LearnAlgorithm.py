# -*- coding: utf-8 -*-
__author__ = 'Raymond'

import networkx as nx
from networkx.algorithms import bipartite
from networkx.algorithms import is_directed_acyclic_graph

import heapq

from blist import sortedlist

def prog_04(fname):
    n = None
    l = list()

    f = open(fname)
    n = eval(f.readline())
    for v in f.readline().strip().split():
        l.append(eval(v))
    f.close()

    print l

    cnt = 0
    for i in xrange(1,n):
        k = i
        while k>0:
            if l[k]<l[k-1]:
                l[k],l[k-1]=l[k-1],l[k]
                cnt += 1
            k-=1

    print l
    print cnt

def prog_05(fname):
    f = open(fname)
    value, num = f.readline().strip().split()
    value = eval(value)
    num = eval(num)

    relation = {}
    for line in f:
        k,v = line.strip().split()
        k,v = eval(k),eval(v)
        if k in relation:
            relation[k].append(v)
        else:
            relation[k]=[v]
        if v in relation:
            relation[v].append(k)
        else:
            relation[v] = [k]
    f.close()

    res = []
    for k in xrange(1,value+1):
        cnt = 0
        if k in relation:
            relat = relation[k]
            for rel_v in relat:
                cnt +=len(relation[rel_v])

        res.append(cnt)

    for r in res:
        print r,


def prog_06(fname):
    f = open(fname)
    row, col = f.readline().strip().split()
    row, col = eval(row),eval(col)

    res = []
    for line in f:
        var = line.strip().split()
        for i,v in enumerate(var):
            var[i]=eval(v)

        e_v = -1
        for v in var:
            cnt = var.count(v)
            if cnt > col/2:
                e_v = v

        res.append(e_v)

    # print res

    for r in res:
        print r,


    f.close()


def prog_07(fname):
    f = open(fname)
    n1 = eval(f.readline().strip())
    s1 = f.readline().strip().split()
    for i,v in enumerate(s1):
        s1[i]=eval(v)

    n2 = eval(f.readline().strip())
    s2 = f.readline().strip().split()
    for i,v in enumerate(s2):
        s2[i] = eval(v)
    f.close()

    res = []

    while s1 or s2:
        m1,m2 = None, None
        if s1: m1 = s1[0]
        if s2: m2 = s2[0]

        if m1 is None:
            res.append(m2)
            s2.remove(m2)
        if m2 is None:
            res.append(m1)
            s1.remove(m1)
        if m1 is not None and m2 is not None:
            res.append(min(m1,m2))
            if res[-1]==m1:
                s1.remove(m1)
            elif res[-1]==m2:
                s2.remove(m2)


    for r in res:
        print r,



def prog_08(fname):
    f = open(fname)
    row,col = f.readline().strip().split()
    row,col = eval(row),eval(col)

    res = {}

    for i,line in enumerate(f):
        s = line.strip().split()
        for j,v in enumerate(s):
            s[j]=eval(v)

        # print s

        for j,v in enumerate(s):
            if -v in s[j+1:]:
                res[i]=[s.index(v)+1,j+1+s[j+1:].index(-v)+1]
        if i not in res:
            res[i] = [-1]

    f.close()

    ks = res.keys()
    ks.sort()

    for k in ks:
        for r in res[k]:
            print r,
        print


def prog_09(fname):
    f = open(fname)

    value,num = f.readline().strip().split()
    value,num = eval(value),eval(num)

    graph = nx.DiGraph()
    for line in f:
        o1,o2 = line.strip().split()
        o1,o2 = eval(o1),eval(o2)
        graph.add_edge(o1,o2)


    f.close()

    print graph.nodes()
    print graph.edges()

    result = nx.shortest_path_length(graph,1)
    print '='*100

    for v in xrange(1,value+1):
        print result.get(v,-1),

    #################################################

    f = open(fname)

    m,n = map(int, f.readline().strip().split())

    g = [set() for i in xrange(m+1)]

    for line in f:
        u,v = map(int, line.strip().split())
        g[u].add(v)


    f.close()

    d = [-1 for i in xrange(m+1)]

    d[1] = 0
    q = [1]

    while q:
        u = q.pop(0)
        for v in g[u]:
            if d[v]==-1:
                q.append(v)
                d[v] = d[u]+1

    print d[1:]


def prog_10(fname):
    f = open(fname)
    value,num = f.readline().strip().split()
    value,num = eval(value),eval(num)

    graph = nx.Graph()
    for line in f:
        o1,o2 = line.strip().split()
        o1,o2 = eval(o1),eval(o2)
        graph.add_edge(o1,o2)

    for node in xrange(1,value+1):
        graph.add_node(node)

    f.close()

    cnt = 0
    for c in nx.connected_components(graph):
        print c
        cnt += 1

    print cnt

    #########################################################
    f = open(fname)

    value, num = map(int, f.readline().strip().split())

    g = [set() for i in xrange(value+1)]

    for line in f:
        u,v = map(int, line.strip().split())
        g[u].add(v)
        g[v].add(u)

    f.close()

    print g

    d = [False for i in xrange(value+1)]

    def explore(g,v,d):
        d[v] = True
        for u in g[v]:
            if not d[u]:
                explore(g,u,d)

    cnt = 0
    for i in xrange(1,value+1):
        if not d[i]:
            explore(g,i,d)
            cnt += 1

    print cnt


def prog_11(fname):
    f = open(fname)

    n = map(int, f.readline().strip())

    l = map(int, f.readline().strip().split())

    f.close()

    print n
    print l

    heapq._heapify_max(l)
    f = open('result.dat','w')
    for v in l:
        f.write(str(v)+'\t')
    f.close()

def prog_12(fname):
    f = open(fname)

    n = map(int, f.readline().strip())
    l = map(int, f.readline().strip().split())

    f.close()

    print l
    from blist import sortedlist

    l = sortedlist(l)

    print l

    f = open('result.dat','w')
    for i in l:
        f.write(str(i)+'\t')
    f.close()


def prog_13(fname):
    f = open(fname)

    n = map(int, f.readline().strip())
    l = map(int, f.readline().strip().split())

    f.close()

    print l

    a = l[0]

    from blist import sortedlist
    l = sortedlist(l)
    l.remove(a)

    l.add(a)

    with open('result.dat','w') as f:
        for i in l:
            f.write(str(i)+'\t')


def prog_14(fname):
    d = {}
    from blist import sortedlist
    import bisect

    with open(fname) as f:
        for i,line in enumerate(f):
            v = map(int, line.strip().split())
            # v = sortedlist(v)
            v = list(v)
            d[i]=v
            # v.bisect

    # def sum3(l):
    #     num = l
    #     num.sort()
    #     res = []
    #     for i in range(len(num)-2):
    #         if i == 0 or num[i] > num[i-1]:
    #             left = i + 1; right = len(num) - 1
    #             while left < right:
    #                 if num[left] + num[right] == -num[i]:
    #                     res.append([num[i], num[left], num[right]])
    #                     left += 1; right -= 1
    #                     while left < right and num[left] == num[left-1]: left +=1
    #                     while left < right and num[right] == num[right+1]: right -= 1
    #                 elif num[left] + num[right] < -num[i]:
    #                     while left < right:
    #                         left += 1
    #                         if num[left] > num[left-1]: break
    #                 else:
    #                     while left < right:
    #                         right -= 1
    #                         if num[right] < num[right+1]: break
    #     return res

    # def sum3(num):
    #     num.sort()
    #     res = []
    #     if len(num) < 3:
    #         return res
    #     for i in xrange(len(num)-2):
    #         if i > 0 and num[i-1] == num[i]:
    #             continue
    #         target = -num[i]
    #         j, k = i+1, len(num) - 1
    #         while j < k:
    #             if j > i+1 and num[j] == num[j-1]:
    #                 j += 1
    #                 continue
    #             if num[j] + num[k] > target:
    #                 k -= 1
    #             elif num[j] + num[k] < target:
    #                 j += 1
    #             else:
    #                 res.append([num[i], num[j], num[k]])
    #                 j, k = j + 1, k - 1
    #     return res

    # def sum3(num):
    #     res = []
    #     # sortnum = sorted(num)
    #
    #     sortnum = num
    #
    #     length = len(sortnum)
    #
    #     # make sure a < b < c
    #     for i in xrange(length-2):
    #         a = sortnum[i]
    #         # remove duplicate a
    #         if i >= 1 and a == sortnum[i-1]:
    #             continue
    #         j = i + 1
    #         k = length - 1
    #         while j < k:
    #             b = sortnum[j]
    #             c = sortnum[k]
    #             if b + c == -a:
    #                 res.append([a,b,c])
    #                 # remove duplicate b,c
    #                 while j < k:
    #                     j += 1
    #                     k -= 1
    #                     if sortnum[j] != b or sortnum[k] != c:
    #                         break
    #             elif b + c > -a:
    #                 # remove duplicate c
    #                 while j < k:
    #                     k -= 1
    #                     if sortnum[k] != c:
    #                         break
    #             else:
    #                 # remove duplicate b
    #                 while j < k:
    #                     j += 1
    #                     if sortnum[j] != b:
    #                         break
    #     return res


    # def sum3(v):
    #     for i in xrange(len(v)-2):
    #         k = len(v)-1
    #         while k-i>2:
    #
    #             a = v[i]
    #             b = v[k]
    #             c = 0-a-b
    #             if c in v[i:k]:
    #                 return (i,v.index(c),k)
    #             else:
    #                 k-=1

    # for k,v in d.iteritems():
    #     if len(v)<3:continue
    #     # print k, sum3(v)
    #     res = sum3(v)
    #     if not res:
    #         print -1
    #     else:
    #         flg = False
    #         for a,b,c in res:
    #             ia = v.index(a)
    #             ib = v.index(b)
    #             ic = v.index(c)
    #             ia += 1
    #             ib += 1
    #             ic += 1
    #             if ia < ib and ib < ic:
    #                 print ia,ib,ic
    #                 flg = True
    #                 break
    #         if not flg:
    #             print -1
            # print v.index(a)+1,v.index(b)+1,v.index(c)+1

    # print sum3(d[1])


    # with open('result.dat','w') as f:
    #     for k,v in d.iteritems():
    #         if len(v)<3:continue
    #         res = sum3(v)
    #         if res is None:
    #             f.write('-1\n')
    #         else:
    #             for rv in res:
    #                 f.write(str(rv)+'\t')
    #             f.write('\n')


    def triple_sum(l):
        n = len(l)

        l = sorted(l)

        for i in xrange(n-2):
            i = i
            j = i+1
            k = n-1
            while j<k:

                a = l[i]
                b = l[j]
                c = l[k]
                if a+b+c==0:
                    return (a,b,c)
                if a+b+c>0:
                    k-=1
                else:
                    j+=1

    for k,v in d.iteritems():
        res = triple_sum(v)
        if not res:
            print -1
        else:
            t = [v.index(res[0]),v.index(res[1]),v.index(res[2])]
            t.sort()
            print t[0]+1,t[1]+1,t[2]+1



def prog_15(fname):

    graphs = {}
    f = open(fname)
    n = map(int, f.readline().strip().split())
    n = n[0]
    f.readline()
    for i in xrange(n):
        graph = nx.Graph()
        line = f.readline()
        while line:
            edges = map(int, line.strip().split())

            graph.add_edge(edges[0],edges[1])
            line = f.readline()
            # print line
            line = line.strip()
            # print 'xxxxx   ',line

        graphs[i]=graph

    f.close()

    for k,g in graphs.iteritems():
        if bipartite.is_bipartite(g):
            print 1,
        else:
            print -1,

def prog_16(fname):

    graphs = {}
    f = open(fname)
    n = map(int, f.readline().strip().split())
    n = n[0]
    f.readline()
    for i in xrange(n):
        graph = nx.DiGraph()
        line = f.readline()
        while line:
            edges = map(int, line.strip().split())

            graph.add_edge(edges[0],edges[1])
            line = f.readline()
            # print line
            line = line.strip()
            # print 'xxxxx   ',line

        graphs[i]=graph

    f.close()

    print graphs

    for k,g in graphs.iteritems():
        if is_directed_acyclic_graph(g):
            print 1,
        else:
            print -1,


def prog_17(fname):
    f = open(fname)
    graph = nx.DiGraph()
    value,num = map(int, f.readline().strip().split())
    for line in f:
        n1,n2,w = map(int, str(line).strip().split())
        graph.add_weighted_edges_from([(n1,n2,w)])

    graph.add_nodes_from(range(1,value+1))

    f.close()

    lengths = nx.single_source_dijkstra_path_length(graph,1)

    for i in xrange(1,value+1):
        print lengths.get(i,-1),

def prog_18(fname):
    f = open(fname)
    n = eval(f.readline().strip())
    arr = map(int, f.readline().strip().split())
    f.close()

    heapq.heapify(arr)

    with open('result.dat','w') as f:
        for i in xrange(n):
            f.write(str(heapq.heappop(arr))+'\t')


count = 0

def prog_19(fname):
    f = open(fname)
    n = eval(f.readline().strip())
    arr = map(int, f.readline().strip().split())
    f.close()

    # cnt = 0
    # for i in xrange(n-1):
    #     for j in xrange(i+1,n):
    #         if arr[i]>arr[j]:
    #             cnt += 1
    #
    # print cnt

    def InversionsCount(x):
        global count
        midsection = len(x) / 2
        leftArray = x[:midsection]
        rightArray = x[midsection:]
        if len(x) > 1:
            InversionsCount(leftArray)
            InversionsCount(rightArray)
            i, j = 0, 0
            a = leftArray; b = rightArray
            for k in range(len(a) + len(b) + 1):
                if a[i] <= b[j]:
                    x[k] = a[i]
                    i += 1
                    if i == len(a) and j != len(b):
                        while j != len(b):
                            k +=1
                            x[k] = b[j]
                            j += 1
                        break
                elif a[i] > b[j]:
                    x[k] = b[j]
                    count += (len(a) - i)
                    j += 1
                    if j == len(b) and i != len(a):
                        while i != len(a):
                            k+= 1
                            x[k] = a[i]
                            i += 1
                        break
    InversionsCount(arr)
    print count

    fileIn = open(fname)
    raw = fileIn.read().split('\n')[1]
    arrayA = [int(i) for i in raw.split()]
    arrayB = sorted(arrayA)
    noInversion = 0
    while len(arrayA) > 0:
        b = arrayB.index(arrayA[0])
        noInversion += b
        # arrayB.pop(arrayB.index(arrayA[0]))
        arrayB.pop(b)
        arrayA.pop(0)

    print noInversion
    fileIn.close()


def prog_20(fname):
    graph = nx.DiGraph()
    f = open(fname)
    value, num = map(int, f.readline().strip().split())
    for line in f:
        e1,e2,weight = map(int, line.strip().split())
        graph.add_weighted_edges_from([(e1,e2,weight)])
    graph.add_nodes_from(xrange(1,value+1))
    f.close()

    pred, dist = nx.bellman_ford(graph,1)

    for i in xrange(1,value+1):
        print dist.get(i, 'x'),

def prog_21(fname):

    f = open(fname)
    n = eval(f.readline().strip())

    graphs = {}

    for i in xrange(n):
        nodes,num = map(int, f.readline().strip().split())
        graph = nx.DiGraph()
        fe = None

        for j in xrange(num):
            e1,e2,w = map(int, f.readline().strip().split())
            if j==0:
                fe = (e1,e2)
            graph.add_weighted_edges_from([(e1,e2,w)])

        graphs[i]={'graph':graph, 'edge':fe}

    f.close()

    # print graphs


    for i in xrange(n):
        graph = graphs[i]['graph']
        fe    = graphs[i]['edge']

        try:
            print nx.dijkstra_path_length(graph,fe[0],fe[1])+nx.dijkstra_path_length(graph,fe[1],fe[0]),
        except:
            print -1,
        # cs = nx.simple_cycles(graph)
        # flg = False
        # for c in cs:
        #     if fe[0] in c and fe[1] in c:
        #         print nx.dijkstra_path_length(graph,c[0],c[-1])+nx.dijkstra_path_length(graph,c[-1],c[0]),
        #         flg = True
        #         break
        # if not flg:
        #     print -1,

def prog_22(fname):
    f = open(fname)

    num = eval(f.readline().strip())

    arr = map(int, f.readline().strip().split())

    k = eval(f.readline().strip())

    arr = sorted(arr)
    # arr = sortedlist(arr)

    # print arr[k-1]
    for i in xrange(k):
        print arr[i],
    f.close()

def prog_23(fname):
    graph = nx.DiGraph()
    f = open(fname)
    next(f)
    for line in f:
        e1,e2 = map(int, line.strip().split())
        graph.add_edge(e1,e2)
    f.close()

    ts = nx.topological_sort(graph)
    for n in ts:
        print n,

def prog_24(fname):
    import sys
    sys.setrecursionlimit(10**5)
    f = open(fname)
    n = eval(f.readline().strip())
    graphs = {}
    # f.readline()
    for i in xrange(n):
        vs,es = map(int, f.readline().strip().split())
        graph = nx.DiGraph()
        # graph.add_nodes_from(range(1,vs+1))
        for j in xrange(es):
            e1,e2 = map(int, f.readline().strip().split())
            graph.add_edge(e1,e2)

        graphs[i]=graph

    f.close()

    # def hamilton(G):
    #     F = [(G,[G.nodes()[0]])]
    #     n = G.number_of_nodes()
    #     while F:
    #         graph,path = F.pop()
    #         confs = []
    #         for node in graph.neighbors(path[-1]):
    #             conf_p = path[:]
    #             conf_p.append(node)
    #             conf_g = nx.Graph(graph)
    #             conf_g.remove_node(path[-1])
    #             confs.append((conf_g,conf_p))
    #         for g,p in confs:
    #             if len(p)==n:
    #                 return p
    #             else:
    #                 F.append((g,p))
    #     return None

    with open('result.dat','w') as f:
        f.write('\n')

    for i in xrange(n):
        graph = graphs[i]

        ns = sorted(graph.nodes())
        lpath = nx.dag_longest_path(graph)
        if len(ns) == len(lpath):
            print 1,
            for p in lpath:
                print p,
            print
        else:
            print -1

        with open('result.dat','a') as f:
            if len(ns) == len(lpath):
                f.write(str(1)+'\t')
                for p in lpath:
                    f.write(str(p)+'\t')
                f.write('\n')
            else:
                f.write('-1\n')


        # if tournament.is_tournament(graph):
        #     print 1,
        #     for p in tournament.hamiltonian_path(graph):
        #         print p,
        #     print
        # else:
        #     print -1
        # print tournament.hamiltonian_path(graph)
        #
        # print 'Done'
        # with open('result.dat','a') as f:
        #     res = tournament.hamiltonian_path(graph)
        #     for i in res:
        #         f.write(str(i)+'\t')
        #     f.write("\n")
        # # res = tournament.hamiltonian_path(graph)
        # for i in res:
        #     print i,


def prog_25(fname):
    graphs = {}

    f = open(fname)

    ns = eval(f.readline().strip())
    for i in xrange(ns):
        graph = nx.DiGraph()
        nds,eds = map(int, f.readline().strip().split())
        for j in xrange(eds):
            e1,e2,w = map(int, f.readline().strip().split())
            graph.add_weighted_edges_from([(e1,e2,w)])

        graphs[i]=graph


    f.close()

    for i in xrange(ns):
        graph = graphs[i]
        if nx.negative_edge_cycle(graph):
            print 1,
        else:
            print -1,

    # negative_edge_cycle

def prog_26(fname):
    f = open(fname)
    n = eval(f.readline().strip())
    arr = map(int, f.readline().strip().split())

    f.close()

    sarr = sortedlist(arr)

    with open('result.dat','w') as f:
        for a in sarr:
            print a,
            f.write(str(a)+'\t')

def prog_27(fname):
    graph = nx.DiGraph()
    f = open(fname)

    ns,es = map(int, f.readline().strip().split())

    graph.add_nodes_from(range(1,ns+1))

    for line in f:
        e1,e2 = map(int, line.strip().split())
        graph.add_edge(e1,e2)

    f.close()

    print nx.is_strongly_connected(graph)
        # print 'xxxxxxxx'

    print nx.number_strongly_connected_components(graph)

def prog_29(fname):
    graphs = {}

    f = open(fname)

    n = eval(f.readline().strip())

    f.readline() # space \n line

    for i in xrange(n):
        graph = nx.DiGraph()

        line = f.readline().strip()
        while line:
            e1,e2 = map(int, line.split())
            graph.add_edge(e1,e2)
            line = f.readline().strip()

        graphs[i] = graph


    f.close()

    for i in xrange(n):
        graph = graphs[i]

        # print nx.all_pairs_node_connectivity(graph)
        # print nx.topological_sort(graph)
        # n for n,d in G.in_degree().items() if d==0
        nds = list(graph.nodes())
        res = None
        for nd in graph.nodes():
            ns = len(nx.shortest_path_length(graph,nd))
            if ns == len(nds):
                res = nd

        if res:
            print res,
        else:
            print -1,
                # print i,nd
        # res = []
        # # cnt = 0
        # for n,d in graph.in_degree().iteritems():
        #     if d == 0:
        #         # print i,n
        #         # cnt +=1
        #         res.append(n)
        #
        # for rn in res:
        #     ps = nx.shortest_path_length(graph,rn)
        #     if len(ps)==len(nds):
        #         print i,rn
        #     else:
        #         print i,-1


        # print nds
        # for idx in xrange(len(nds)-1):
        #     print nx.node_connectivity(graph,nds[idx],nds[idx+1]) or nx.node_connectivity(graph,nds[idx+1],nds[idx])


    # semi-connected problem.
    # for i in xrange(n):
    #     graph = graphs[i]
    #
    #     flg = nx.is_semiconnected(graph)
    #     if flg:
    #         print 1,
    #     else:
    #         print -1,

        # nodes = list(graph.nodes())
        # for i in xrange(len(nodes)):
        #     n1 = nodes[i]
        #     for j in xrange(len(nodes)):
        #         n2 = nodes[j]
        #         if i != j:
        #             print nx.node_connectivity(graph,n1,n2),
        #             print nx.node_connectivity(graph,n2,n1),
        #
        # print nx.node_connectivity(graph)

        # np = nx.all_pairs_node_connectivity(graph)
        #
        # flg = False
        # for k,v in np.iteritems():
        #     vs = v.values()
        #     if not 0 in vs:
        #         flg = True
        #         print k,
        #         break
        #
        # if not flg:
        #     print -1,


def prog_30(fname):
    graph = nx.DiGraph()
    f = open(fname)
    ns,es = map(int, f.readline().strip().split())
    graph.add_nodes_from(range(1,ns+1))
    for line in f:
        e1,e2,w = map(int, line.strip().split())
        graph.add_weighted_edges_from([(e1,e2,w)])
    f.close()

    pres,dist = nx.bellman_ford(graph,1);
    # print pres
    for i in xrange(1,ns+1):
        if i in dist:
            print dist[i],
        else:
            print 'x',

    with open('result.dat','w') as f:
        for i in xrange(1,ns+1):
            if i in dist:
                f.write(str(dist[i])+'\t')
            else:
                f.write('x\t')




def prog_28(fname):

    # TODO:::::::::::::::::::::::::::
    from formula import Formula
    import solver

    formulas = {}

    f = open(fname)

    ns = eval(f.readline().strip())
    f.readline()

    for i in xrange(ns):
        formula = Formula()


        line = f.readline().strip()
        cnt = 0
        while line:
            if cnt == 0:
                line = f.readline().strip()
                cnt +=1
                continue
            e1,e2 = map(int, line.split())
            formula.add_clause((e1,e2))
            line = f.readline().strip()

        formulas[i] = formula


    f.close()

    # print random_formula(2,6)

    for i in xrange(ns):
        formula = formulas[i]
        # print formula
        flg = solver.satisfiable(formula)
        if flg:
            print 1,
            sg = max(solver.find_component(formula), key=len)

            for n in sorted(sg):
                print n,



        else:
            print 0,

        print



if __name__ == '__main__':
    import sys
    args = sys.argv

    if args[1] == '-04':
        prog_04(args[2])

    if args[1] == '-05':
        prog_05(args[2])

    if args[1] == '-06':
        prog_06(args[2])

    if args[1] == '-07':
        prog_07(args[2])

    if args[1] == '-08':
        prog_08(args[2])

    if args[1] == '-09':
        prog_09(args[2])

    if args[1] == '-10':
        prog_10(args[2])

    if args[1] == '-11':
        prog_11(args[2])

    if args[1] == '-12':
        prog_12(args[2])

    if args[1] == '-13':
        prog_13(args[2])

    if args[1] == '-14':
        prog_14(args[2])

    if args[1] == '-15':
        prog_15(args[2])

    if args[1] == '-16':
        prog_16(args[2])

    if args[1] == '-17':
        prog_17(args[2])

    if args[1] == '-18':
        prog_18(args[2])

    if args[1] == '-19':
        prog_19(args[2])

    if args[1] == '-20':
        prog_20(args[2])

    if args[1] == '-21':
        prog_21(args[2])

    if args[1] == '-22':
        prog_22(args[2])

    if args[1] == '-23':
        prog_23(args[2])

    if args[1] == '-24':
        prog_24(args[2])

    if args[1] == '-25':
        prog_25(args[2])

    if args[1] == '-26':
        prog_26(args[2])

    if args[1] == '-27':
        prog_27(args[2])

    if args[1] == '-28':
        prog_28(args[2])

    if args[1] == '-29':
        prog_29(args[2])

    if args[1] == '-30':
        prog_30(args[2])