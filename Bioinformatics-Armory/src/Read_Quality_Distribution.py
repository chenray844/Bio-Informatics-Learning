from Bio import SeqIO

avg = 21

def main(fname):
    records = list(SeqIO.parse(fname,'fastq'))

    num = 0
    for record in records:
        vs = record.letter_annotations['phred_quality']
        if sum(vs)/float(len(vs)) < avg:
            num += 1
    print num

    # record = records[0]
    # print record.letter_annotations['phred_quality']

if __name__ == '__main__':
    import sys, os
    fname = os.path.join(os.getcwd(),sys.argv[-1])
    main(fname)