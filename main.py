from Bio.Seq import Seq

dna_dog = "ATGTGTGTCTGCTCGCT"
dna_cat = "ATGCGTGATGATGCGAT"

hybrid = Seq(dna_dog + dna_cat)

print(hybrid)