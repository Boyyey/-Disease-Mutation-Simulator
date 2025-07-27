import streamlit as st

def about_page():
    """Streamlit About/Help page for the Disease Mutation Simulator."""
    st.markdown("""
    ## Project Description
    A web app to visualize and predict likely future mutations in viral proteins (e.g., SARS‑CoV‑2, Influenza, HIV) using real sequence data, AI/ML, and interactive 3D protein structures.

    ## Features
    - Upload or select viral strains (FASTA or built-in)
    - ML-based mutation prediction (Random Forest/XGBoost/Transformer)
    - Interactive 3D protein structure (py3Dmol)
    - Heatmap/bar chart of predicted mutation probabilities
    - Hypothetical mutant design
    - Antibody escape risk prediction
    - Multi-strain comparison & mutation trajectory
    - Advanced analytics & generative models
    - Beautiful, annotated, scientific UI/UX

    ## Credits
    - Built with ❤️ using open-source tools
    - Data: GISAID, NCBI Virus, Influenza Research Database
    - Visualization: py3Dmol, Plotly, Streamlit
    - ML: scikit-learn, XGBoost, PyTorch

    ---
    *Prototype: For demo/educational use. Not for clinical decisions.*
    """) 