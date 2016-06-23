from nwck_class_3 import Newick_Tree
import numpy as np
f=open('data/data.dat')
junk=f.readline()
s1=f.readline().strip()
s2=f.readline().strip()
f.close()

n=Newick_Tree(s1)
m=Newick_Tree(s2)
X=np.zeros((3,3,max(n.tree.keys())+2,len(m.tree.keys())+2))
#Z=np.zeros((3,3,max(n.tree.keys())+2,len(m.tree.keys())+2))

def xchoose2(r):
    if r<2:
        return 0
    else:
        return(r*(r-1)/2)

def xchoose4(r):
    if r<4:
        return 0
    else:
        return((1.0*r*(r-1)*(r-2)*(r-3))/24)

Nspan={}
for x in n.post_order(n.root):
    if len(n.dtree[x])==0:
        Nspan[x]=1
    else:
        Nspan[x]=sum([Nspan[i] for i in n.dtree[x]])

Mspan={}
for x in m.post_order(m.root):
    if len(m.dtree[x])==0:
        Mspan[x]=1
    else:
        Mspan[x]=sum([Mspan[i] for i in m.dtree[x]])


#X=defaultdict(int)

for A in n.leaves_postordered:
    for B in m.leaves_postordered:
        Aindex=n.dtree[n.tree[A]].index(A)
        Bindex=m.dtree[m.tree[B]].index(B)
        Aparent=n.tree[A]
        Bparent=m.tree[B]
        if n.node_to_taxon[A]==m.node_to_taxon[B]:
 #           X[0,0,A,B]=1
 #           X[Aindex,0,Aparent,B]=1
 #           X[0,Bindex,A,Bparent]=1
            X[Aindex,Bindex,Aparent,Bparent]=1

Q=0
for A in n.post_order(n.dtree[n.root][0]):
    for B in m.post_order(m.dtree[m.root][0]):
        Aindex=n.dtree[n.tree[A]].index(A)
        Bindex=m.dtree[m.tree[B]].index(B)
        Aparent=n.tree[A]
        Bparent=m.tree[B]
        if len(n.dtree[A])==2 and len(m.dtree[B])==2:
            #X[Aindex,Bindex,Aparent,Bparent]=X[0,0,A,B]+X[0,1,A,B]+X[1,0,A,B]+X[1,1,A,B]
            X[0,Bindex,A,Bparent]=X[0,0,A,B]+X[0,1,A,B]
            X[1,Bindex,A,Bparent]=X[1,0,A,B]+X[1,1,A,B]
            X[Aindex,0,Aparent,B]=X[0,0,A,B]+X[1,0,A,B]
            X[Aindex,1,Aparent,B]=X[0,1,A,B]+X[1,1,A,B]
            X[Aindex,Bindex,Aparent,Bparent]=X[0,0,A,B]+X[0,1,A,B]+X[1,0,A,B]+X[1,1,A,B]
            X[0,2,A,B]=Nspan[n.dtree[A][0]]-X[0,0,A,B]-X[0,1,A,B]
            X[1,2,A,B]=Nspan[n.dtree[A][1]]-X[1,0,A,B]-X[1,1,A,B]
            X[2,0,A,B]=Mspan[m.dtree[B][0]]-X[1,0,A,B]-X[0,0,A,B]
            X[2,1,A,B]=Mspan[m.dtree[B][1]]-X[0,1,A,B]-X[1,1,A,B]
            X[2,2,A,B]=len(n.taxa)-Nspan[n.dtree[A][0]]-Nspan[n.dtree[A][1]]-X[2,1,A,B]-X[2,0,A,B]
#            Q+=(xchoose2(X[2,2,A,B])*(X[0,0,A,B]*X[1,1,A,B]+X[1,0,A,B]*X[0,1,A,B]))

#for A in n.post_order(n.dtree[n.root][0]):
#    for B in m.post_order(m.dtree[m.root][0]):
#      if len(n.dtree[A])==0 or len(m.dtree[B])==0:
#          continue
#      else:
#        X[0,2,A,B]=Nspan[n.dtree[A][0]]-X[0,0,A,B]-X[0,1,A,B]
#        X[1,2,A,B]=Nspan[n.dtree[A][1]]-X[1,0,A,B]-X[1,1,A,B]
#        X[2,0,A,B]=Mspan[m.dtree[B][0]]-X[1,0,A,B]-X[0,0,A,B]
#        X[2,1,A,B]=Mspan[m.dtree[B][1]]-X[0,1,A,B]-X[1,1,A,B]
#        X[2,2,A,B]=len(n.taxa)-Nspan[n.dtree[A][0]]-Nspan[n.dtree[A][1]]-X[2,1,A,B]-X[2,0,A,B]
ds=[]
for A in n.post_order(n.dtree[n.root][0]):
    for B in m.post_order(m.dtree[m.root][0]):
      if len(n.dtree[A])==0 or len(m.dtree[B])==0:
          continue
      else:
        pA=n.tree[A]
        pB=m.tree[B]
        Aindex=n.dtree[pA].index(A)
        Bindex=m.dtree[pB].index(B)
        Z00AB=X[1-Aindex,1-Bindex,pA,pB]
        Z11AB=X[2,2,pA,pB]
        Z01AB=X[1-Aindex,2,pA,pB]
        Z10AB=X[2,1-Bindex,pA,pB]
        ZZ02AB=X[1-Aindex,Bindex,pA,pB]
        Z20AB=X[Aindex,1-Bindex,pA,pB]
        Z12AB=X[2,Bindex,pA,pB]
        Z21AB=X[Aindex,2,pA,pB]
        Z22AB=X[Aindex,Bindex,pA,pB]
        dqX=xchoose2(X[2,2,A,B])*(X[0,0,A,B]*X[1,1,A,B]+X[1,0,A,B]*X[0,1,A,B])
        dqZ=xchoose2(Z22AB)*(Z00AB*Z11AB+Z10AB*Z01AB)
        U00AB=X[0,1-Bindex,A,pB]
        U10AB=X[1,1-Bindex,A,pB]
        U01AB=X[0,2,A,pB]
        U11AB=X[1,2,A,pB]
        U22AB=X[1-Aindex,0,pA,B]+X[2,0,pA,B]+X[1-Aindex,1,pA,B]+X[2,1,pA,B]
        dqU=xchoose2(U22AB)*(U00AB*U11AB+U10AB*U01AB)
        V00AB=X[1-Aindex,0,pA,B]
        V10AB=X[1-Aindex,1,pA,B]
        V01AB=X[2,0,pA,B]
        V11AB=X[2,1,pA,B]
        V22AB=X[0,1-Bindex,A,pB]+X[0,2,A,pB]+X[1,1-Bindex,A,pB]+X[1,2,A,pB]
        dqV=xchoose2(V22AB)*(V00AB*V11AB+V10AB*V01AB)
        if dqX!=0 or dqZ!=0 or dqU!=0 or dqV!=0:
            ds.append((A,B,dqX,dqZ,dqU,dqV))
        #print A,B,dqX,dqZ
        Q+=dqX+dqZ+dqU+dqV

print 2*xchoose4(len(n.taxa))-Q

def tsummary(X,A,B):
    return [(i,j,X[i,j,A,B]) for i in [0,1,2] for j in [0,1,2]]