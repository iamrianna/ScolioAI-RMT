import streamlit as st

st.set_page_config(
    page_title="Scolio-AI - Scoliosis Screening Assistant",
    page_icon="🦴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Light-theme styling with dark navy and teal accents
st.markdown("""
    <style>
    .stApp {
        background-color: #F8FAFC;
        color: #0F172A;
    }
    .main-title {
        color: #0F2942;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 2.25rem;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        color: #008080;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #E2E8F0;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #008080;
        color: white;
        border-radius: 8px;
        font-weight: 600;
        border: none;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #006666;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title Header
st.markdown('<div class="main-title">Scolio-AI — Scoliosis Screening Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Developed by Rianna-Maria Tanase</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>Welcome to Scolio-AI</h3>
    <p>An artificial intelligence research tool designed to evaluate standing full-spine radiographs for signs of scoliosis using deep convolutional network features and Grad-CAM interpretability overlays.</p>
    <p><b>Please select an action from the navigation sidebar on the left:</b></p>
    <ul>
        <li><b>🔍 Analyze:</b> Upload DICOM or standard image files for screening and Grad-CAM feature analysis.</li>
        <li><b>📊 Model Performance:</b> Review test metrics, confusion matrices, and model limitation benchmarks.</li>
        <li><b>📚 Education & Safety:</b> Learn about scoliosis assessment protocols and AI limitations.</li>
        <li><b>🔒 Privacy & Terms:</b> View data handling procedures and responsible use disclaimers.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.info("⚠️ **Clinical Disclaimer:** Scolio-AI is a decision support research aid and does NOT provide definitive diagnostic verdicts or calculate exact clinical Cobb angles.")
