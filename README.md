# 🧬🧪 Disease Mutation Simulator

A web app to visualize and predict likely future mutations in viral proteins (e.g., SARS‑CoV‑2, Influenza, HIV) using real sequence data, AI/ML, and interactive 3D protein structures.

## 🚀 Features
- Upload or select viral strains (FASTA or built-in)
- Dummy AI/ML mutation prediction (MVP)
- Interactive 3D protein structure (py3Dmol)
- Heatmap/bar chart of predicted mutation probabilities
- Intuitive, scientific, and beautiful UI

## 🛠️ Tech Stack
- Streamlit (web app)
- Biopython (sequence parsing)
- py3Dmol (3D protein visualization)
- Plotly (heatmap/bar chart)
- numpy (dummy prediction)

## 📦 Installation
```bash
pip install -r requirements.txt
```

## ▶️ How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
2. **(Optional) Add built-in strain FASTA files**
   - Place FASTA files for built-in strains in the `data/` directory (e.g., `data/wuhan.fasta`).
3. **Launch the app**
   ```bash
   streamlit run app.py
   ```
4. **Open in your browser**
   - Streamlit will provide a local URL (e.g., http://localhost:8501). Open it in your browser.

### Troubleshooting
- If you see errors about missing data files, add the required FASTA files to the `data/` directory or use the upload feature.
- If you get errors about missing Python packages, ensure you have installed all dependencies from `requirements.txt`.
- For advanced features (e.g., ML models), you may need to install extra dependencies or download model files.

## 📝 How it works
1. **Upload** a viral sequence (FASTA) or select a known strain
2. **Predict** mutation hotspots (dummy model for MVP)
3. **Visualize** on 3D protein structure and heatmap

## 🌟 Why it’s cool
- Blends bioinformatics, AI/ML, and protein visualization
- Helps scientists and the public understand viral evolution
- Could aid vaccine design and variant tracking

## 📚 Data sources
- [GISAID](https://www.gisaid.org/)
- [NCBI Virus](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/)
- [Influenza Research Database](https://www.fludb.org/)

## 🙏 Credits
- Built with ❤️ using open-source tools

---
*Prototype: For demo/educational use. Not for clinical decisions.* 