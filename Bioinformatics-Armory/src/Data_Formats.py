# >>>from Bio import Entrez
# >>>from Bio import SeqIO
# >>>Entrez.email = "your_name@your_mail_server.com"
# >>>handle = Entrez.efetch(db="nucleotide", id=["FJ817486, JX069768, JX469983"], rettype="fasta")
# >>>records = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format
# >>>print records[0].id  #first record id
# gi|227437129|gb|FJ817486.1|
# >>>print len(records[-1].seq)  #length of the last record
# 771

from Bio import Entrez
from Bio import SeqIO

def main():
    ids = 'NR_073358 JX491654 JX280897 NM_001131214 FJ817486 JQ762396 HM595636 JX317624 JX393321'
    ids = ', '.join(ids.split())
    Entrez.email = 'crf1111@126.com'
    handle = Entrez.efetch(db='nucleotide', id=[ids], rettype='fasta')
    records = list(SeqIO.parse(handle, 'fasta'))

    records = sorted(records, key=len)
    print '>',records[0].description
    print records[0].seq



if __name__ == '__main__':
    main()