import streamlit as st
import numpy as np
from ml.ensemble import EnsembleMutationPredictor

def ensemble_demo_ui(strain, features):
    """Streamlit UI to demo the ensemble mutation predictor (stub)."""
    st.subheader("Ensemble Model Demo")
    st.write("Shows predictions from Random Forest, XGBoost, Transformer, and the ensemble.")
    ensemble = EnsembleMutationPredictor()
    preds = ensemble.predict(features, strain.sequence)
    st.line_chart(preds)
    st.write("Current weights:", ensemble.weights)
    # TODO: Show individual model predictions, allow weight adjustment 