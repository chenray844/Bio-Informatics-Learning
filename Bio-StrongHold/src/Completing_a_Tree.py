import os
import sys

import networkx as nx

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-1])
    f = open(fpath, 'r')
    lines = f.readlines()
    f.close()

    graph = nx.Graph()
    n = int(lines[0].strip())
    graph.add_nodes_from(range(1,n+1))
    for idx in xrange(1,len(lines)):
        line = lines[idx]
        edges = map(int, line.strip().split())

        graph.add_edge(edges[0],edges[1])
    print graph.number_of_nodes()-graph.number_of_edges()-1

if __name__ == '__main__':
    main(*sys.argv)