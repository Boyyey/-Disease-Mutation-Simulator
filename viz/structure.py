import streamlit as st
import py3Dmol
import numpy as np
from data.strain import ViralStrain
from ml.predictor import MutationPrediction

def highlight_residues(view, residues, color='red'):
    """Highlight specific residues in the 3D view."""
    for res in residues:
        view.addStyle({"resi": str(res)}, {"stick": {"color": color}})

def show_structure(strain: ViralStrain, prediction: MutationPrediction, overlays=None, color_by=None, annotation=None):
    """
    Display the 3D structure with mutation hotspots highlighted, overlays for multiple strains, color by property, and annotation (stubs).
    """
    view = py3Dmol.view(query=f"pdb:{strain.pdb_id}")
    view.setStyle({"cartoon": {"color": "spectrum"}})
    view.zoomTo()
    hotspots = np.argsort(-prediction.probabilities)[:10] + 1  # 1-based
    highlight_residues(view, hotspots.tolist(), color='red')
    # Overlays for other strains (stub)
    if overlays:
        for overlay in overlays:
            highlight_residues(view, overlay['hotspots'], color='blue')
    # Color by property (stub)
    if color_by is not None:
        pass  # TODO: color structure by property
    # Annotation (stub)
    if annotation:
        pass  # TODO: add annotation to 3D view
    # view.show()  # REMOVED
    # st.py3dmol(view, height=400)  # REMOVED
    html = view._make_html()
    st.components.v1.html(html, height=400, scrolling=False) 