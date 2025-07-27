import streamlit as st
from utils.constants import STRAINS

def multi_strain_comparison_ui(strain, predictor, features):
    """Streamlit UI for multi-strain comparison and mutation trajectory animation (stub)."""
    st.subheader("Multi-strain Comparison & Mutation Trajectory")
    with st.expander("Compare with another strain"):
        compare_strain = st.selectbox("Select strain to compare:", list(STRAINS.keys()))
        if st.button("Compare"):
            st.write(f"Comparing {strain.name} with {compare_strain}")
            # TODO: Load and compare, show overlays, animate mutation trajectory 