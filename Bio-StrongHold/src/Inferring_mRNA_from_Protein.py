from Bio.SeqUtils.CodonUsage import SynonymousCodons
from Bio.SeqUtils import seq1

import sys
import os

fpath = os.path.join(os.getcwd(),sys.argv[-1])

f = open(fpath, 'r')
protein = f.readline().rstrip()
f.close()

#Codon dictionary of just possibility counts (e.g. Met = 1, Ala = 4)
codonTable = {}
for key in SynonymousCodons.keys():
    # Use seq1 to convert three letter codes to one letter
    codonTable[seq1(key)] = len(SynonymousCodons[key])

# Amino acid combinations
aa_comb = 1
for aa in protein:
    aa_comb *= codonTable[aa]

# Times 3 for the 3 possible stop codons
# Modulo 1000000 to make final number reasonable sized
print aa_comb * 3 % 1000000