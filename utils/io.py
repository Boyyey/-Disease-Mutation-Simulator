import os
import json
import pandas as pd
from Bio import SeqIO

def read_fasta(filepath):
    """Read a FASTA file and return a list of SeqRecord objects."""
    with open(filepath) as f:
        return list(SeqIO.parse(f, "fasta"))

def write_fasta(records, filepath):
    """Write a list of SeqRecord objects to a FASTA file."""
    with open(filepath, 'w') as f:
        SeqIO.write(records, f, "fasta")

def read_csv(filepath):
    """Read a CSV file into a pandas DataFrame."""
    return pd.read_csv(filepath)

def write_csv(df, filepath):
    """Write a pandas DataFrame to a CSV file."""
    df.to_csv(filepath, index=False)

def read_json(filepath):
    """Read a JSON file and return the data."""
    with open(filepath) as f:
        return json.load(f)

def write_json(data, filepath):
    """Write data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def log(message, level="INFO"):
    print(f"[{level}] {message}") 