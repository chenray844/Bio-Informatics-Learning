# -*- utf-8 -*-
import os

from numpy import zeros
import numpy as np


MONOISOTOPIC_MASS_TABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}

class StrongHold(object):
    def __init__(self):
        pass

    @staticmethod
    def parserDNAFile(fname):
        f = open(fname,'r')
        str = f.read()
        f.close()
        return str

    @staticmethod
    def two_dna(fname):
        f = open(fname, 'r')
        s1 = f.readline().strip()
        s2 = f.readline().strip()
        f.close()
        return s1,s2



class Algorithm(object):
    def __init__(self):
        pass

    @staticmethod
    def hammingDistance(s1, s2):
        """Return the Hamming distance between equal-length sequences"""
        if len(s1) != len(s2):
            raise ValueError("Undefined for sequences of unequal len"
                             "gth")
        return sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s1, s2))

    @staticmethod
    def fib_mortal(n,m):
        # track number
        # track age of each
        fib_table = []
        for i in range(n):
            if i < 2:
                fib_table.append(1)
            elif i < m:
                fib_table.append(fib_table[-2] + fib_table[-1])
            elif i == m or i == m+1:
                fib_table.append((fib_table[-2] + fib_table[-1]) - 1)
            else:
                fib_table.append((fib_table[-2] + fib_table[-1]) - fib_table[-(m+1)])
        return fib_table[-1]

    @classmethod
    def find_shortest_superstring(self,DNAs,superstring=''):
        DNAs = list(DNAs)
        if len(DNAs)==0:
            return superstring

        elif len(superstring)==0:
            superstring = DNAs.pop(0)
            return self.find_shortest_superstring(DNAs,superstring)

        else:
            for i in xrange(len(DNAs)):
                dna = DNAs[i]
                length = len(dna)

                for p in xrange(length/2):
                    q = length - p

                    if superstring.startswith(dna[p:]):
                        DNAs.pop(i)
                        return self.find_shortest_superstring(DNAs, dna[:p]+superstring)

                    if superstring.endswith(dna[:q]):
                        DNAs.pop(i)
                        return self.find_shortest_superstring(DNAs, superstring+dna[q:])

    @classmethod
    def catalan_number(self, rna, lo, hi, dp):
        mapping = {
            'A':'U',
            'U':'A',
            'G':'C',
            'C':'G',
        }
        characters = hi - lo +1
        if characters % 2 == 1:
            return 0

        if lo >= hi or lo >= len(rna) or hi < 0:
            return 1

        if (lo, hi) in dp:
            return dp[(lo,hi)]
        else:
            curr = rna[lo]
            target = mapping[curr]
            acc = 0
            for i in xrange(lo+1, hi+1, 2):
                if rna[i] == target:
                    left = self.catalan_number(rna, lo+1, i-1, dp)
                    right = self.catalan_number(rna, i+1, hi, dp)
                    acc += (left*right) % 1e6
            dp[(lo,hi)] = acc
            return acc

    @classmethod
    def KMP_failure_table(self, seq):
        failure_array = [0]*len(seq)
        k = 0
        for i in range(2, len(seq)):
            # check if substring can be expanded
            # print i, k, seq[k], seq[i-1]
            # if subsequence (k > 0) but sequence doesn't continue
            while k > 0 and seq[k] != seq[i-1]:
                # reset k index to 1 before ending character to avoid repetition
                k = failure_array[k-1]
            # if subsequence starting or continuing
            if seq[k] == seq[i-1]:
                k += 1
                # -1 for 0-indexing
            failure_array[i-1] = k
        return failure_array

    @classmethod
    def longest_common_subsequence(self, dna1, dna2):
        '''Returns the longest longest common subsequence of dna1 and dna2.'''
        # Compute each entry of M.
        M = zeros((len(dna1)+1,len(dna2)+1))
        for i in xrange(len(dna1)):
            for j in xrange(len(dna2)):
                if dna1[i] == dna2[j]:
                    M[i+1][j+1] = M[i][j]+1
                else:
                    M[i+1][j+1] = max(M[i+1][j],M[i][j+1])

        # Recover a maximum substring.
        longest_sseq = ''
        i,j = len(dna1), len(dna2)
        while i*j != 0:
            if M[i][j] == M[i-1][j]:
                i -= 1
            elif M[i][j] == M[i][j-1]:
                j -= 1
            else:
                longest_sseq = dna1[i-1] + longest_sseq
                i -= 1
                j -= 1

        return longest_sseq

    @classmethod
    # Function to calculate distance proportion
    def pDistance(self, s1, s2):
        total = float(len(s1))
        count = 0
        for i in xrange(len(s1)):
            if s1[i] == s2[i]:
                count += 1
        return 1.0 - float(count)/float(total)

    @classmethod
    def Motzkin_Numbers(self, rna, noncross):
        mapping = {
            'A':'U',
            'U':'A',
            'G':'C',
            'C':'G',
        }
        if len(rna) <=1:
            return 1
        else:
            if rna in noncross:
                return noncross[rna]
            else:
                subintervals = []
                for i in xrange(1,len(rna)):
                    if rna[0] == mapping[rna[i]]:
                        subintervals.append([rna[1:i], rna[i+1:]])
                noncross[rna] = (sum([self.Motzkin_Numbers(subint[0], noncross)*self.Motzkin_Numbers(subint[1], noncross)
                                      for subint in subintervals]) + self.Motzkin_Numbers(rna[1:], noncross)) % int(1e6)

            return noncross[rna]


###################################################################################################################
#######        https://github.com/jschendel/Rosalind/blob/master/scripts/Newick_Trees.py               ############
#######                                                                                                ############
###################################################################################################################
'''A ROSALIND bioinformatics script to parse trees given in Newick format.'''


class Node(object):
    '''Node class for Newick Trees.'''
    def __init__(self, number, parent, name=None):
        '''Node initialization.'''
        self.number = number
        self.parent = parent
        self.children = []
        self.name = [name, 'Node_' + str(self.number)][name is None]

    def __repr__(self):
        '''Defines how Node instances are printed.'''
        return ['Node_' + str(self.number) + '('+str(self.name)+')', str(self.name)+'()'][self.name == 'Node_'+str(self.number)]

    def add_child(self, child):
        '''Add a child to the node.'''
        self.children.append(child)


class Newick(object):
    '''Creates a Newick Tree from the given data.'''
    def __init__(self, data):
        '''Initialize the Newick Tree.'''
        self.nodes = []
        self.node_index = 0
        self.edges = []
        self.construct_tree(data)
        self.name_index = {node.name: node.number for node in self.nodes}

    def construct_tree(self, data):
        '''Constructs the Newick Tree.'''
        data = data.replace(',', ' ').replace('(','( ').replace(')',' )').strip(';').split()
        current_parent = Node(-1, None)
        for item in data:
            if item[0] == '(':
                current_parent = Node(len(self.nodes), current_parent.number)
                self.nodes.append(current_parent)
                if len(self.nodes) > 1:
                    self.nodes[current_parent.parent].add_child(current_parent.number)
                    self.edges.append((current_parent.parent, current_parent.number))

            elif item[0] == ')':
                if len(item) > 1:
                    current_parent.name = item[1:]
                current_parent = self.nodes[current_parent.parent]

            else:
                self.nodes[current_parent.number].add_child(len(self.nodes))
                self.edges.append((current_parent.number, len(self.nodes)))
                self.nodes.append(Node(len(self.nodes), current_parent.number, item))

    def edge_names(self):
        '''Return a list of edges referencing node names.'''
        return [(self.nodes[edge[0]].name, self.nodes[edge[1]].name) for edge in self.edges]

    def distance(self, name1, name2):
        '''Returns the distance between name1 and name2.'''
        if name1 == name2:
            return 0

        # Create the branches from the two desired nodes to the root.
        branch1 = [self.name_index[name1]]
        branch2 = [self.name_index[name2]]
        while self.nodes[branch1[-1]].parent != -1:
            branch1.append(self.nodes[branch1[-1]].parent)
        while self.nodes[branch2[-1]].parent != -1:
            branch2.append(self.nodes[branch2[-1]].parent)

        return len(set(branch1) ^ set(branch2)) + 1

    def get_descendants(self, node_name):
        descendants = []
        for child in self.nodes[self.name_index[node_name]].children:
            descendants.append(self.nodes[child].name)
            descendants += self.get_descendants(self.nodes[child].name)

        return descendants


class WeightedNewick(object):
    '''Creates a Newick Tree from the given data.'''
    def __init__(self, data):
        '''Initialize the Newick Tree.'''
        self.nodes = []
        self.node_index = 0
        self.edges = []
        self.node_weight = {}
        self.construct_tree(data)
        self.name_index = {node.name: node.number for node in self.nodes}

    def construct_tree(self, data):
        '''Constructs the Newick Tree.'''
        data = data.replace(',', ' ').replace('(','( ').replace(')',' )').strip(';').split()
        current_parent = Node(-1, None)
        for item in data:
            if item[0] == '(':
                current_parent = Node(len(self.nodes), current_parent.number)
                self.nodes.append(current_parent)
                if len(self.nodes) > 1:
                    self.nodes[current_parent.parent].add_child(current_parent.number)
                    self.edges.append((current_parent.parent, current_parent.number))

            elif item[0] == ')':
                if len(item) > 1:
                    self.node_weight[current_parent.number] = int(item[item.find(':') + 1:])
                    if len(item) > 2:
                        current_parent.name = item[1:item.find(':')]
                current_parent = self.nodes[current_parent.parent]

            else:
                self.nodes[current_parent.number].add_child(len(self.nodes))
                self.edges.append((current_parent.number, len(self.nodes)))
                self.node_weight[len(self.nodes)] = int(item[item.find(':') + 1:])
                self.nodes.append(Node(len(self.nodes), current_parent.number, item[:item.find(':')]))

    def edge_names(self):
        '''Return a list of edges referencing node names.'''
        return [(self.nodes[edge[0]].name, self.nodes[edge[1]].name) for edge in self.edges]

    def distance(self, name1, name2):
        '''Returns the distance between name1 and name2.'''
        if name1 == name2:
            return 0

        # Create the branches from the two desired nodes to the root.
        branch1 = [self.name_index[name1]]
        branch2 = [self.name_index[name2]]
        while self.nodes[branch1[-1]].parent != -1:
            branch1.append(self.nodes[branch1[-1]].parent)
        while self.nodes[branch2[-1]].parent != -1:
            branch2.append(self.nodes[branch2[-1]].parent)

        return sum([self.node_weight[node] for node in set(branch1) ^ set(branch2)])

    def get_descendants(self, node_name):
        descendants = []
        for child in self.nodes[self.name_index[node_name]].children:
            descendants.append(self.nodes[child].name)
            descendants += self.get_descendants(self.nodes[child].name)

        return descendants

class BLOSUM62(object):
    """The BLOSUM62 scoring matrix class."""

    def __init__(self):
        """Initialize the scoring matrix."""
        with open(os.path.join(os.path.dirname(__file__), 'data/BLOSUM62.dat')) as input_data:
            items = [line.strip().split() for line in input_data.readlines()]
            self.scoring_matrix = {(item[0], item[1]):int(item[2]) for item in items}

    def __getitem__(self, pair):
        """Returns the score of the given pair of protein."""
        return self.scoring_matrix[pair[0], pair[1]]


class SuffixTree(object):
    '''Creates a suffix tree for the provided word.'''

    def __init__(self, word):
        '''Initializes the suffix tree.'''
        self.nodes = [self.Node(None, 0)]
        self.edges = dict()
        self.descendants_dict = dict()
        if type(word) == str:
            self.add_word(word)

    class Node(object):
        '''Suffix tree node class.'''
        def __init__(self, parent, number):
            self.parent = parent
            self.number = number
            self.children = []

        def add_child(self, child):
            self.children.append(child)

        def remove_child(self, child):
            self.children.remove(child)

        def update_parent(self, parent):
            self.parent = parent

    def add_word(self, word):
        '''Add a word to the suffix tree.'''
        # Check to make sure word ends in '$'.
        if word[-1] != '$':
            word += '$'
        self.word = word
        self.n = len(self.word)

        for i in xrange(self.n):
            parent_node, edge_start, overlap = self.insert_position(i, self.nodes[0])

            if overlap:
                p_edge_start, p_edge_end = self.edges[(parent_node.parent.number, parent_node.number)]

                # Get the edge to insert
                insert_len = 0
                while word[edge_start:edge_start + insert_len] == word[p_edge_start:p_edge_start + insert_len]:
                    insert_len += 1

                # Create a new node for insertion
                new_node = self.Node(parent_node.parent, len(self.nodes))
                new_node.add_child(parent_node)
                self.add_node(parent_node.parent, p_edge_start, p_edge_start + insert_len - 1, new_node)

                # Update the parent node since a new node is inserted above it
                del self.edges[(parent_node.parent.number, parent_node.number)]
                parent_node.parent.remove_child(parent_node)
                parent_node.update_parent(new_node)
                self.edges[(parent_node.parent.number, parent_node.number)] = [p_edge_start + insert_len - 1, p_edge_end]

                # Add new child node
                self.add_node(new_node, edge_start + insert_len - 1, self.n)

            else:
                # No insertion necessary, just append the new node.
                self.add_node(parent_node, edge_start, self.n)

    def insert_position(self, start_index, parent_node):
        '''Determine the location and method to insert a suffix into the suffix tree.'''
        for child_node in parent_node.children:
            edge_start, edge_end = self.edges[(parent_node.number, child_node.number)]
            if self.word[start_index:start_index + edge_end - edge_start] == self.word[edge_start:edge_end]:
                return self.insert_position(start_index + edge_end - edge_start, child_node)

            elif self.word[edge_start] == self.word[start_index]:
                return child_node, start_index,  True

        return parent_node, start_index, False

    def add_node(self, parent_node, edge_start, edge_end, child_node=None):
        '''Adds a node and the associated edge to the suffix tree.'''

        # Create child node, if necessary
        if child_node is None:
            child_node = self.Node(parent_node, len(self.nodes))

        # Add node to node list
        self.nodes.append(child_node)

        # Add child to parent
        parent_node.add_child(child_node)

        # Add edge to edge dict
        self.edges[(parent_node.number, child_node.number)] = [
            edge_start, edge_end]

    def print_edges(self):
        '''Returns the string representations of the edges.'''
        return [self.word[i:j] for i, j in self.edges.values()]

    def total_descendants(self, base_node):
        '''Returns the total number of descendants of a given node.'''
        if base_node not in self.descendants_dict:
            self.descendants_dict[base_node] = len(base_node.children) + sum([self.total_descendants(c) for c in base_node.children])

        return self.descendants_dict[base_node]

    def node_word(self, end_node):
        '''Returns the prefix of the suffix tree word up to a given node.'''
        current_word = ''
        while end_node.number != 0:
            temp_indices = self.edges[(end_node.parent.number, end_node.number)]
            current_word = self.word[temp_indices[0]:temp_indices[1]] + current_word
            end_node = end_node.parent

        return current_word.strip('$')


class Newick_Tree:
    def __init__(self,s):
        (self.tree,self.labels,self.weights,self.taxa)=self.build_tree2(s)
        self.parents=np.unique(self.tree.values())
        self.string=s


    def tokens(self,s):
        cursor=0
        n=''
        while cursor<len(s):
            if s[cursor]=='(':
                cursor+=1
                yield 'OPEN_PAREN','('
                continue
            if s[cursor]==')':
                cursor+=1
                yield 'CLOSE_PAREN',')'
                continue
            if s[cursor]==':':
                cursor+=1
                yield 'COLON',':'
            if s[cursor]==';':
                cursor=len(s)
                break

            if s[cursor]==',':
                cursor+=1
                yield 'COMMA',','
                continue
            n=''
            while cursor<len(s) and s[cursor] not in [',',';',')','(',':']:
                n+=s[cursor]
                cursor+=1
            if len(n.strip())>0:
                yield 'LABEL',n.strip()

    def build_tree2(self,s):
        tree,labels,weights={},{},{}
        taxa=[]
        parent,curnode,savenode=-1,0,0
        new_node=1
        tree[0]=-1 #introduce an artificial root note
        prior_kind=None
        for (kind,value) in self.tokens(s):
            if kind=='OPEN_PAREN':
                parent=curnode
                curnode=new_node
                tree[curnode]=parent
                new_node=new_node+1
                prior_kind=kind
                continue
            if kind=='LABEL':
                if prior_kind=='CLOSE_PAREN':
                    labels[value]=savenode
                elif prior_kind=='COLON':
                    weights[savenode]=int(value)
                else:
                    labels[value]=new_node
                    tree[new_node]=curnode
                    savenode=new_node # needed if this label is followed by colon
                    taxa.append(value)
                    new_node+=1
                prior_kind=kind
                continue

            if kind=='COLON':
                if prior_kind=='COMMA' or prior_kind=='OPEN_PAREN':
                    tree[new_node]=curnode
                #savenode=new_node
                new_node+=1
                prior_kind=kind
                continue

            if kind=='CLOSE_PAREN':
                if prior_kind=='COMMA':
                    tree[new_node]=curnode
                    new_node+=1
                savenode=curnode
                curnode=parent
                parent=tree[curnode]
                prior_kind=kind
                continue
            if kind=='COMMA':
                if prior_kind=='COMMA':
                    tree[new_node]=curnode
                    new_node+=1
                prior_kind=kind
                continue

        if parent!=-1:
            raise Exception('ParseError')
        else:
            return tree,labels,weights,taxa


    def path_to_root(self,x):
        tree=self.tree
        start_node=labels[x]
        path=[start_node]
        parent=tree[start_node]
        while parent!=-1:
            path.append(parent)
            parent=tree[parent]
        return path

    def common_ancestor(self,x,y):
        tree,labels,weights=self.tree,self.labels,self.weights
        xnode=labels[x]
        ynode=labels[y]
        d=0
        while True:
            if xnode<ynode:
                d+=weights.get(ynode,1)
                ynode=tree[ynode]
            elif ynode<xnode:
                d+=weights.get(xnode,1)
                xnode=tree[xnode]
            elif ynode==xnode:
                return xnode

    def distance(self,x,y):
        tree,labels,weights=self.tree,self.labels,self.weights
        xnode=labels[x]
        ynode=labels[y]
        d=0
        while True:
            if xnode<ynode:
                d+=weights.get(ynode,1)
                ynode=tree[ynode]
            elif ynode<xnode:
                d+=weights.get(xnode,1)
                xnode=tree[xnode]
            elif ynode==xnode:
                return d

    def path(self,x,y):
        tree,labels,weights=self.tree,self.labels,self.weights
        xnode=labels[x]
        ynode=labels[y]
        front=[]
        back=[]
        while True:
            if xnode<ynode:
                back.insert(0,ynode)
                ynode=tree[ynode]
            elif xnode>ynode:
                front.append(xnode)
                xnode=tree[xnode]
            elif ynode==xnode:
                back.insert(0,ynode)
                front.extend(back)
                return front

    def separates(self,a,x,y):
        tree,labels,weights=self.tree,self.labels,self.weights
        b=tree[a]
        xnode=labels[x]
        ynode=labels[y]
        front=[]
        back=[]
        has_a,has_b=False,False
        while True:
            if xnode==a or ynode==a:
                has_a=True
            if ynode==b or xnode==b:
                has_b=True
            if xnode<ynode:
                back.insert(0,ynode)
                ynode=tree[ynode]
            elif xnode>ynode:
                front.append(xnode)
                xnode=tree[xnode]
            elif ynode==xnode:
                back.insert(0,ynode)
                front.extend(back)
                return (has_a and has_b)


    def char_table(self):
        base=self.taxa[0]
        answer=[]
        for x in self.parents:
            if x<1:
                continue
            row=''
            for t in sorted(self.taxa):
                row+=str(int(self.separates(x,base,t)))
            answer.append(row)
        return(answer[1:])