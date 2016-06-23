
# from StringIO import StringIO
# from Bio import Phylo
#
# if __name__ == '__main__':
#     fid = open('data/Counting_DNA_Nucleotides.dat','r')
#     pairs = [l2.split('\n') for l2 in fid.read().strip().split('\n\n')]
#     for s, line2 in pairs:
#
#         x, y = line2.split()
#         tree = Phylo.read(StringIO(s), 'newick')
#         print tree.count_terminals(),
#         print tree.distance(x,y), # 0,0,,,,, it may be biopython's bug

'''
Newick class is designed by jschendel( https://github.com/jschendel/Rosalind/blob/master/scripts/Newick_Trees.py).

Thanks.

'''

from StrongHold import Newick

with open('data/data.dat') as input_data:
	trees = [line.split('\n') for line in input_data.read().strip().split('\n\n')]

# The majority of the work is done by the Newick class in the Data Structures script.
distances = [str(Newick(tree[0]).distance(*tree[1].split())-1) for tree in trees]

# Print and save the answer.
print ' '.join(distances)

        


