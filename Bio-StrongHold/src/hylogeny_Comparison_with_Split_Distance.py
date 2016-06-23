from StrongHold import Newick_Tree

with open("data/data.dat","rU") as f:
    taxa=f.readline().split()
    newick_1=f.readline().strip()
    newick_2=f.readline().strip()

t1=Newick_Tree(newick_1)
t2=Newick_Tree(newick_2)

char1=set(t1.char_table())
char2=set(t2.char_table())

delta=char1.symmetric_difference(char2)
print len(delta)