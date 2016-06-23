# allows use of Python3.X print functionality
from __future__ import print_function
import re # for regex functions

import sys
import os

# need regex for N-glycosylation motif
# N{any but P}[S or T]{any but P}
# parentheses and '?=' allow for overlapping
motif = re.compile('(?=N[^P][ST][^P])')

# loop through protein id's to import from uniprot website
import urllib2
from Bio import SeqIO

def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(), args[-2])
    dataset = open(fpath, 'r')
    protein_ids = dataset.readlines()
    dataset.close()

    out_path = os.path.join(os.getcwd(), args[-1])
    outhandle = open(out_path, 'w')
    uniprot_url = "http://www.uniprot.org/uniprot/"

    for protein in protein_ids:
        request = urllib2.Request("".join([uniprot_url+protein.rstrip()+".fasta"]))
        opener = urllib2.build_opener()
        f = opener.open(request)
        raw_data = SeqIO.read(f, 'fasta')
        f.close()

        locations = []
        # Use search instead of match to search entire string
        if re.search(motif, str(raw_data.seq)):
            print(protein.strip(), file=outhandle)
            for m in re.finditer(motif, str(raw_data.seq)):
                locations.append(m.start()+1)
            print(" ".join(map(str, locations)), file=outhandle)

    outhandle.close()

if __name__ == '__main__':
    main(*sys.argv)