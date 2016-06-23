import os
import sys

from Bio import SeqIO
from Bio.Data import CodonTable


def main(*args, **kwargs):
    fpath = os.path.join(os.getcwd(),args[-1])
    record = SeqIO.read(fpath, 'fasta')

    standard_table = CodonTable.unambiguous_dna_by_name['Standard']
    stop_codons = standard_table.stop_codons

    def chunker(seq, size):
        return (seq[pos:pos+size] for pos in xrange(0, len(seq), size))

    proteins = set()
    for strand in [record.seq, record.seq.reverse_complement()]:
        for start in xrange(len(strand)-2):
            start_codon = str(strand[start:start+3])
            if start_codon == 'ATG':
                frame = str(strand[start:])
                if any(st in chunker(frame[3:], 3) for st in stop_codons):
                    prot = str(strand[start:].translate(to_stop=True))
                    proteins.add(prot)

    for prot in proteins:
        print prot


if __name__ == "__main__":
    main(*sys.argv)