from Bio import Align

align = Align.PairwiseAligner()
Seq1 = "ATCGAAAAAAAAA"
Seq2 = "ATCAAAGCCCCA"

# Global alignment
count = 0
alignments = align.align(Seq1, Seq2)
for alignment in alignments:
    print(alignment)
    count += 1
score = align.score(Seq1, Seq2)
print(f'The number of alignments is {count}')
print(f'The score for the pairwise alignment is {score}')
