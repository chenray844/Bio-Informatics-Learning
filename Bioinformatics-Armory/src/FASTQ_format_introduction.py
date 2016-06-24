from Bio import SeqIO

def main(fname, out):
    SeqIO.convert(fname,'fastq',out,'fasta')

if __name__ == '__main__':
    import sys,os
    fname = os.path.join(os.getcwd(),sys.argv[-2])
    out = os.path.join(os.getcwd(), sys.argv[-1])
    main(fname, out)