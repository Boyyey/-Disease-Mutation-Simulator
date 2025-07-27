import streamlit as st
from bio.mutant import design_mutant
from viz.heatmap import show_mutation_heatmap

def mutant_designer_ui(strain, predictor, features, escape_predictor):
    """Streamlit UI for designing and analyzing hypothetical mutants."""
    st.subheader("Hypothetical Mutant Designer")
    with st.expander("Design a mutant (edit sequence)"):
        mutant_pos = st.number_input("Mutation position (1-based)", min_value=1, max_value=len(strain.sequence), value=1)
        mutant_aa = st.text_input("New amino acid (1-letter)", value="A")
        if st.button("Apply Mutation"):
            mutant_seq = design_mutant(strain.sequence, [(mutant_pos-1, mutant_aa)])
            st.write(f"Mutant sequence (first 60): {mutant_seq[:60]}...")
            # Predict and visualize mutant
            mutant_pred = predictor.predict(mutant_seq, features=features)
            st.write("Predicted mutation probabilities for mutant:")
            show_mutation_heatmap(strain, mutant_pred, key="mutant_heatmap")
            mutant_escape = escape_predictor.predict_escape(mutant_seq)
            st.write(f"Predicted antibody escape risk: {mutant_escape:.2f}") 