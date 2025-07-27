# --- Streamlit Entrypoint for Disease Mutation Simulator ---
import streamlit as st
from data.strain import ViralStrain, fetch_sequence_from_db, parse_fasta, load_cached_data, cache_data
from ml.predictor import MutationPredictor
from ml.features import SequenceFeatureExtractor
from ml.antibody import AntibodyEscapePredictor
from bio.mutant import design_mutant
from viz.structure import show_structure, highlight_residues
from viz.heatmap import show_mutation_heatmap
from utils.constants import STRAINS, DATA_CACHE
from pages.mutant_designer import mutant_designer_ui
from pages.comparison import multi_strain_comparison_ui
from pages.advanced_analysis import advanced_analysis_ui
from pages.sequence_explorer import sequence_explorer_ui
from pages.model_evaluation import model_evaluation_ui
from pages.ensemble_demo import ensemble_demo_ui

st.set_page_config(page_title="🧬🧪 Disease Mutation Simulator", layout="wide")
st.title("🧬🧪 Disease Mutation Simulator")

# --- Sidebar: Strain Selection & Dataset Integration ---
st.sidebar.header("Strain Selection & Data")

uploaded_file = st.sidebar.file_uploader("Upload viral sequence (FASTA)")
selected_strain = st.sidebar.selectbox("Or select known strain:", list(STRAINS.keys()))
accession = st.sidebar.text_input("Or fetch by accession (NCBI/GISAID):", "")
db_choice = st.sidebar.selectbox("Database:", ["ncbi", "gisaid", "influenza"]) 

# --- Main: Sequence Loading ---
if uploaded_file:
    sequence = parse_fasta(uploaded_file)
    pdb_id = "6VXX"
    strain = ViralStrain("Uploaded", sequence, pdb_id)
elif accession:
    cached = load_cached_data(accession)
    if cached:
        sequence = cached
    else:
        sequence = fetch_sequence_from_db(accession, db=db_choice)
        if sequence:
            cache_data(accession, sequence)
    pdb_id = "6VXX"
    strain = ViralStrain(accession, sequence, pdb_id)
elif selected_strain:
    fasta_path, pdb_id = STRAINS[selected_strain]
    try:
        with open(fasta_path) as f:
            sequence = parse_fasta(f)
    except Exception:
        sequence = "M" * 1273
    strain = ViralStrain(selected_strain, sequence, pdb_id)
else:
    st.warning("Please upload a sequence, select a strain, or enter an accession.")
    st.stop()

# --- Feature Extraction ---
feature_extractor = SequenceFeatureExtractor(strain.sequence)
features = feature_extractor.compute_features()

# --- ML Prediction ---
predictor_type = st.sidebar.selectbox("Prediction Model:", ["dummy", "random_forest", "xgboost", "transformer"])
predictor = MutationPredictor(model_type=predictor_type)
prediction = predictor.predict(strain.sequence, features=features)

# --- Antibody Escape Prediction ---
escape_predictor = AntibodyEscapePredictor()
escape_risk = escape_predictor.predict_escape(strain.sequence)

PAGES = {
    "Main App": None,
    "Sequence Explorer": sequence_explorer_ui,
    "Advanced Analytics": advanced_analysis_ui,
    "Model Evaluation": model_evaluation_ui,
    "Ensemble Model Demo": ensemble_demo_ui,
    "About": lambda *_: __import__('pages.about', fromlist=['about_page']).about_page()
}

page = st.sidebar.radio("Navigate", list(PAGES.keys()))

if page == "Main App":
    # --- Main visualizations and UI ---
    st.subheader("3D Protein Structure")
    show_structure(strain, prediction)
    st.subheader("Predicted Mutation Probabilities")
    show_mutation_heatmap(strain, prediction, key="main_heatmap")
    mutant_designer_ui(strain, predictor, features, escape_predictor)
    st.subheader("Antibody Escape Risk")
    st.write(f"Predicted escape risk for current strain: {escape_risk:.2f}")
    multi_strain_comparison_ui(strain, predictor, features)
    st.markdown("""
    ---
    *Prototype: Upload a FASTA, select a strain, or enter an accession to see predicted mutation hotspots, design mutants, and explore antibody escape!*
    """)
else:
    # Call the selected page with appropriate arguments
    if page == "Sequence Explorer":
        sequence_explorer_ui(strain, prediction)
    elif page == "Advanced Analytics":
        advanced_analysis_ui(strain, prediction, features)
    elif page == "Model Evaluation":
        model_evaluation_ui()
    elif page == "Ensemble Model Demo":
        ensemble_demo_ui(strain, features)
    elif page == "About":
        PAGES[page]() 