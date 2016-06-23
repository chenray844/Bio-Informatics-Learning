from Bio import SeqIO
from Bio import Phylo
from cStringIO import StringIO
from sys import argv, stdout

with open('data/data.dat') as f:
    tree = Phylo.read(StringIO(f.readline()), 'newick')
    seqs = dict((record.id, str(record.seq)) for record in SeqIO.parse(f, 'fasta'))
#Phylo.write(tree, stdout, 'newick', plain=True)

# add trivial seqsets to leaves
for name, seq in seqs.items():
    next(tree.find_elements(name=name)).seqset = list({el} for el in seq)

# bottom-up, find letters that match children
def add_seqsets(clade):
    for c in clade.clades:
        add_seqsets(c)
    # all children have been processed!

    try:
        clade.seqset
    except AttributeError:
        child_seqsets = list(child.seqset for child in clade.clades)
        clade.seqset = []
        for pos in zip(*child_seqsets):
            # pos is [{possibilities}, ...]
            intersect = set.intersection(*pos)
            if intersect:
                clade.seqset.append(intersect)
            else:
                union = set.union(*pos)
                clade.seqset.append(union)
                add_seqsets.total_disparsimony += 1
add_seqsets.total_disparsimony = 0

add_seqsets(tree.clade)
print(add_seqsets.total_disparsimony)

# top-down, select values that match parents' selection
def select_best_seq(clade, parent_seq):
    clade.seq = ''
    for parent_val, child_vals in zip(parent_seq, clade.seqset):
        if parent_val in child_vals:
            clade.seq += parent_val
        else:
            clade.seq += list(child_vals)[0]

    if clade.name not in seqs: # internal node
        print('>{}\n{}'.format(clade.name, clade.seq))
            
    for c in clade.clades:
        select_best_seq(c, clade.seq)

# get random initial seq for tree.clade
root_seq = ''
for pos in tree.clade.seqset:
    root_seq += list(pos)[0]
# and start the recursion
select_best_seq(tree.clade, root_seq)