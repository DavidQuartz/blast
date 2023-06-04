from Bio import Align

align = Align.PairwiseAligner()
Seq1 = "ATCGAAAAAAAAA"
Seq2 = "ATCAAAGCCCCA"

# Global alignment
alignments = align.align(Seq1, Seq2)
for alignment in alignments:
    print(alignment)
score = align.score(Seq1, Seq2)
print(f'The score for the pairwise alignment is {score}')
