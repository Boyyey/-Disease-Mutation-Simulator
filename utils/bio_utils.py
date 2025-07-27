from Bio.Seq import Seq
from Bio import pairwise2

def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    return str(Seq(seq).reverse_complement())

def translate(seq):
    """Translate a nucleotide sequence to protein."""
    return str(Seq(seq).translate())

def global_align(seq1, seq2):
    """Perform global alignment between two sequences."""
    alignments = pairwise2.align.globalxx(seq1, seq2)
    return alignments

def local_align(seq1, seq2):
    """Perform local alignment between two sequences."""
    alignments = pairwise2.align.localxx(seq1, seq2)
    return alignments 