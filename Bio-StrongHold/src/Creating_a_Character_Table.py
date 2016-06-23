from numpy import zeros
from StrongHold import Newick

# Read the input data.
with open('data/data.dat') as input_data:
    newick_input = input_data.read().strip()

# Get the Newick tree from the input.
newick_tree = Newick(newick_input)

# Quick lambda functions that will be used to filter named and unnamed nodes.
named_nodes = lambda n: 'Node_' not in n
unnamed_edges = lambda e: 'Node_' in e[0] and 'Node_' in e[1]

# A dictionary relating node name to alphabetical order.
node_order = {name:index for index,name in enumerate(sorted(filter(named_nodes, [node.name for node in newick_tree.nodes])))}

# Get the nontrial edges.
nontrivial_edges = filter(unnamed_edges, newick_tree.edge_names())

# Find and mark the on/off taxa.
M = zeros((len(nontrivial_edges), len(node_order)), dtype=int)
for i, edge in enumerate(nontrivial_edges):
    taxa = filter(named_nodes, set(newick_tree.get_descendants(edge[0])) & set(newick_tree.get_descendants(edge[1])))
    for t in taxa:
        M[i][node_order[t]] = 1

# Print and save the answer.
print '\n'.join([''.join(map(str, M[i])) for i in xrange(len(M))])
