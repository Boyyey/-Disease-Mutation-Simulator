from typing import List, Tuple

def design_mutant(sequence: str, mutations: List[Tuple[int, str]]) -> str:
    """Apply a list of (position, new_aa) mutations to a sequence."""
    seq_list = list(sequence)
    for pos, aa in mutations:
        if 0 <= pos < len(seq_list):
            seq_list[pos] = aa
    return ''.join(seq_list) 