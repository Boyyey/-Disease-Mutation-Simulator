import os
from typing import Optional
from Bio import SeqIO
from utils.constants import DATA_CACHE

class ViralStrain:
    """Represents a viral strain with sequence, PDB ID, and metadata."""
    def __init__(self, name: str, sequence: str, pdb_id: str, metadata: dict = None):
        self.name = name
        self.sequence = sequence
        self.pdb_id = pdb_id
        self.metadata = metadata or {}

def fetch_sequence_from_db(accession: str, db: str = 'ncbi') -> Optional[str]:
    """Fetch a viral sequence from a public database by accession (stub)."""
    # TODO: Real API integration (GISAID/NCBI/Influenza DB)
    if db == 'ncbi':
        return "M" * 1273
    return None

def parse_fasta(file) -> str:
    """Parse a FASTA file and return the sequence as a string."""
    seq_record = next(SeqIO.parse(file, "fasta"))
    return str(seq_record.seq)

def cache_data(key: str, data: str, cache_dir: str = DATA_CACHE):
    os.makedirs(cache_dir, exist_ok=True)
    with open(os.path.join(cache_dir, key + ".fasta"), 'w') as f:
        f.write(data)

def load_cached_data(key: str, cache_dir: str = DATA_CACHE) -> Optional[str]:
    path = os.path.join(cache_dir, key + ".fasta")
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return None 