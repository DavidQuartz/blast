from Bio.Seq import Seq
from Bio import SeqIO

# dna_dog = "ATGTGTGTCTGCTCGCT"
# dna_cat = "ATGCGTGATGATGCGAT"

# hybrid = Seq(dna_dog + dna_cat)

# print(hybrid)

# Working with Fasta file
for seq_record in SeqIO.parse("./nucleotide/sequence.fasta", "fasta"):
    print(seq_record.id)
    print(len(seq_record))
    print(repr(seq_record.seq))

# Working with Genbank file
for seq_record in SeqIO.parse("./nucleotide/sequence.gb", "genbank"):
    print(seq_record.id)
    print(len(seq_record))
    print(repr(seq_record.seq))
