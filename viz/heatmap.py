import streamlit as st
import plotly.graph_objs as go
from data.strain import ViralStrain
from ml.predictor import MutationPrediction
from utils.plot_utils import get_custom_colorscale, apply_plotly_theme, add_scientific_annotations

def show_mutation_heatmap(strain: ViralStrain, prediction: MutationPrediction, overlays=None, colormap='reds', annotation=None, key=None):
    """Display a bar chart of predicted mutation probabilities, with overlays and annotations."""
    fig = go.Figure()
    # Main strain
    fig.add_trace(go.Bar(
        x=list(range(1, len(strain.sequence)+1)),
        y=prediction.probabilities,
        marker=dict(color=prediction.probabilities, colorscale=get_custom_colorscale(colormap)),
        name=strain.name
    ))
    # Overlays for other strains
    if overlays:
        for overlay in overlays:
            fig.add_trace(go.Scatter(
                x=list(range(1, len(overlay['sequence'])+1)),
                y=overlay['probs'],
                mode='lines',
                name=overlay['name'],
                line=dict(width=2, dash='dot')
            ))
    fig.update_layout(
        xaxis_title="Residue Position",
        yaxis_title="Predicted Mutation Probability",
        height=300,
        margin=dict(l=20, r=20, t=30, b=20)
    )
    fig = apply_plotly_theme(fig)
    if annotation:
        fig = add_scientific_annotations(fig, annotation, x=10, y=1)
    st.plotly_chart(fig, use_container_width=True, key=key) 