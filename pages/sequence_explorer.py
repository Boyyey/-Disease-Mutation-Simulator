import streamlit as st
from viz.sequence_view import show_sequence_view

def sequence_explorer_ui(strain, prediction):
    """Streamlit UI for exploring the sequence and mutation probabilities interactively (stub)."""
    st.subheader("Sequence Explorer")
    show_sequence_view(strain.sequence, mutation_probs=prediction.probabilities)
    # TODO: Add click-to-highlight, link to 3D structure, and overlays 