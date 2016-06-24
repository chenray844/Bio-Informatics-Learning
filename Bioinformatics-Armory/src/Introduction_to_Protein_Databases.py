# >>>from Bio import ExPASy
# >>>from Bio import SwissProt
# >>>handle = ExPASy.get_sprot_raw('B5ZC00') #you can give several IDs separated by commas
# >>>record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins

from Bio import ExPASy
from Bio import SwissProt

proten_id = 'Q9QWE9'

handle = ExPASy.get_sprot_raw(proten_id)
record = SwissProt.read(handle)

for item in record.cross_references:
    if len(item)>0 and item[0]=='GO':
        for res in item:
            if str(res).startswith('P:'):
                print str(res)[2:]