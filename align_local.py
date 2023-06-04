from Bio import Align

align = Align.PairwiseAligner()
align.mode = 'local'
Seq1 = 'ATCGA'
Seq2 = 'TCAA'

# Global alignment
count = 0
alignments = align.align(Seq1, Seq2)
for alignment in alignments:
    print(alignment)
    count += 1
score = align.score(Seq1, Seq2)
print(f'The number of alignments is {count}')
print(f'The score for the pairwise alignment is {score}')
