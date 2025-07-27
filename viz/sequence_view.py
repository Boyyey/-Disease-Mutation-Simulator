import streamlit as st
import numpy as np

def show_sequence_view(sequence, mutation_probs=None, highlights=None):
    """Display a colored, interactive sequence view with overlays and click support (stub)."""
    st.write("Sequence view (first 200):")
    colored = ''
    for i, aa in enumerate(sequence[:200]):
        color = 'black'
        if highlights and i in highlights:
            color = 'blue'
        elif mutation_probs is not None:
            # Color by mutation probability (red intensity)
            prob = mutation_probs[i]
            color = f'rgb({int(255*prob)},0,0)'
        colored += f'<span style="color:{color};cursor:pointer" title="Pos {i+1}">{aa}</span>'
    st.markdown(colored, unsafe_allow_html=True)
    # TODO: Add click interactivity, overlays, and full sequence navigation 