import numpy as np
from collections import defaultdict

class Newick_Tree:
    def __init__(self,s):
        (self.tree,self.labels,self.weights,self.taxa,self.dtree,self.label_name)=self.build_tree2(s)
        del self.tree[0]
        del self.tree[1]

        self.parents=np.unique(self.tree.values())
        self.string=s
        self.taxa.sort()
        self.root=self.labels[self.taxa[0]]
        self.reroot_tree(self.root)
        self.min={}
        self.max={}
        self.leaves_postordered=[x for x in self.post_order_leaves(self.root)]
        self.postorder_index=dict(zip(self.leaves_postordered,range(len(self.leaves_postordered))))
        self.chars={}
        self.node_to_taxon={}
        for i,x in enumerate(self.taxa):
            self.node_to_taxon[self.labels[x]]=i
        #self.char_table(self.root)


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
        tree,labels,weights,label_name={},{},{},{}
        dtree=defaultdict(list)
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
                dtree[parent].append(curnode)
                new_node=new_node+1
                prior_kind=kind
                continue
            if kind=='LABEL':
                if prior_kind=='CLOSE_PAREN':
                    labels[value]=savenode
                    label_name[savenode]=value
                elif prior_kind=='COLON':
                    weights[savenode]=int(value)
                else:
                    labels[value]=new_node
                    label_name[new_node]=value
                    tree[new_node]=curnode
                    dtree[curnode].append(new_node)
                    savenode=new_node # needed if this label is followed by colon
                    taxa.append(value)
                    new_node+=1
                prior_kind=kind
                continue

            if kind=='COLON':
                if prior_kind=='COMMA' or prior_kind=='OPEN_PAREN':
                    tree[new_node]=curnode
                    dtree[curnode].append(new_node)
                #savenode=new_node
                new_node+=1
                prior_kind=kind
                continue

            if kind=='CLOSE_PAREN':
                if prior_kind=='COMMA':
                    tree[new_node]=curnode
                    dtree[curnode].append(new_node)
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
            return tree,labels,weights,taxa,dtree,label_name


    def path_to_root(self,x):
        tree=self.tree
        start_node=self.labels[x]
        path=[start_node]
        parent=tree[start_node]
        while parent in tree:
            path.append(parent)
            parent=tree[parent]
        path.append(parent)
        return path

    def path_to_root_nodes(self,x):
        path=[x]
        while True:
            try:
                #print path
                parent=self.tree[x]
            except KeyError:
                return path
            path.append(parent)
            x=parent


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

#    def separates(self,a,x,y):
#        tree,labels,weights=self.tree,self.labels,self.weights
#        b=tree[a]
#        xnode=labels[x]
#        ynode=labels[y]
#        front=[]
#        back=[]
#        has_a,has_b=False,False
#        while True:
#            if xnode==a or ynode==a:
#                has_a=True
#            if ynode==b or xnode==b:
#                has_b=True
#            if xnode<ynode:
#                back.insert(0,ynode)
#                ynode=tree[ynode]
#            elif xnode>ynode:
#                front.append(xnode)
#                xnode=tree[xnode]
#            elif ynode==xnode:
#                back.insert(0,ynode)
#                front.extend(back)
#                return (has_a and has_b)


    def char_table(self,base):
        self.chars[base]=[0]*len(self.taxa)
        #print base
        if len(self.dtree[base])==0:
            self.chars[base][self.node_to_taxon[base]]=1
            return
        else:
            for x in self.dtree[base]:
                self.char_table(x)
            for x in self.dtree[base]:
                for i,y in enumerate(self.chars[x]):
                    if y==1:
                        self.chars[base][i]=1

    def char_table_print(self,base):
        while len(self.dtree[base])==1:
            base=self.dtree[base][0]
        for y in self.dtree[base]:
            for x in self.post_order(y):
                if len(self.dtree[x])==0:
                    continue
                else:
                    print ''.join(map(str,self.chars[x]))


    def post_order(self,base):
        for x in self.dtree[base]:
            for x in self.post_order(x):
                yield x
        yield base

    def post_order_leaves(self,base):
        for x in self.dtree[base]:
            for x in self.post_order(x):
                if len(self.dtree[x])==0:
                    yield x

    def reroot_tree(self,target):
        p=self.path_to_root_nodes(target)
        node=p[0]
        try:
            self.dtree[self.tree[target]].remove(target)
        except KeyError:
            pass
        try:
            self.dtree[target].append(self.tree[target])
        except KeyError:
            pass
        try:
            del self.tree[target]
        except KeyError:
            pass
        for x in p[1:]:
            try:
                self.dtree[self.tree[x]].remove(x)
            except KeyError:
                pass
            try:
                self.dtree[x].append(self.tree[x])
            except KeyError:
                pass
            try:
                self.tree[x]=node
            except KeyError:
                pass
            node=x

    def split_list(self,base):
       if len(self.dtree[base])==0:
           self.min[base]=self.postorder_index[base]
           self.max[base]=self.postorder_index[base]
         #  self.width[base]=self.max[base]-self.min[base]
           return
       else:
           for x in self.dtree[base]:
               self.split_list(x)
           self.min[base]=min([self.min[x] for x in self.dtree[base]])
           self.max[base]=max([self.max[x] for x in self.dtree[base]])
        #   self.width[base]=self.max[base]-self.min[base]
           return