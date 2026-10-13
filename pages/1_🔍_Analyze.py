import streamlit as st
from PIL import Image
import numpy as np
import time
from utils.dicom_handler import load_uploaded_image
from utils.model_engine import run_inference_and_gradcam
from utils.pdf_generator import generate_pdf_report

st.header("Scoliosis Screening Analysis")

# Persistent state initialization
if "analysis_results" not in st.session_state:
    st.session_state["analysis_results"] = None
if "uploaded_image" not in st.session_state:
    st.session_state["uploaded_image"] = None

# Upload / Action Area at Top
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("1. Select or Upload Full-Spine Radiograph")
    
    col_u1, col_u2 = st.columns([2, 1])
    with col_u1:
        uploaded_file = st.file_uploader(
            "Drag & drop DICOM (.dcm), PNG, or JPG radiographs here",
            type=["dcm", "dicom", "png", "jpg", "jpeg"]
        )
    with col_u2:
        st.write("--- OR ---")
        if st.button("Try Licensed Sample Image"):
            sample_img = Image.open("assets/sample_scoliosis.png") if False else Image.new('RGB', (512, 1024), color='#333333')
            st.session_state["uploaded_image"] = sample_img
            st.session_state["filename"] = "Sample_Radiograph_Deidentified.png"

    if uploaded_file is not None:
        img, fname = load_uploaded_image(uploaded_file)
        st.session_state["uploaded_image"] = img
        st.session_state["filename"] = fname

    st.markdown('</div>', unsafe_allow_html=True)

# Main Processing Flow
if st.session_state["uploaded_image"] is not None:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col_prev, col_act = st.columns([1, 2])
    
    with col_prev:
        st.image(st.session_state["uploaded_image"], caption="Image Preview", use_container_width=True)
        
    with col_act:
        st.subheader("2. Run AI Screening Engine")
        st.caption("Supported: Anteroposterior (AP) standing radiographs.")
        
        if st.button("Analyze Image"):
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
            
            results = run_inference_and_gradcam(st.session_state["uploaded_image"])
            st.session_state["analysis_results"] = results
            st.success("Analysis Complete")

    st.markdown('</div>', unsafe_allow_html=True)

# Display Results
if st.session_state["analysis_results"] is not None:
    res = st.session_state["analysis_results"]
    
    if res["status"] == "UNRELIABLE":
        st.warning(f"⚠️ **Unable to Assess Reliably:** {res['reason']}")
    else:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("3. Screening Output & Explainability")
        
        # Results Metric Display
        m1, m2 = st.columns(2)
        m1.metric("Predicted Category", res["predicted_class"])
        m2.metric("Calibrated Confidence", f"{res['confidence']*100:.1f}%")
        
        st.info(f"**Plain-Language Explanation:** {res['explanation']}")
        st.caption("🔍 *Note: Heatmaps highlight attention regions used for classification. They do NOT represent a definitive diagnosis or Cobb angle measurement.*")
        
        # View Switcher
        view_type = st.radio("Select Display View:", ["Original Image", "Grad-CAM Heatmap", "Blended Overlay"], horizontal=True)
        
        if view_type == "Original Image":
            st.image(st.session_state["uploaded_image"], use_container_width=True)
        elif view_type == "Grad-CAM Heatmap":
            st.image(res["heatmap"], use_container_width=True)
        else:
            st.image(res["overlay"], use_container_width=True)
            
        # PDF Generation Button
        pdf_data = generate_pdf_report(st.session_state["filename"], res)
        st.download_button(
            label="📄 Download Diagnostic Summary Report (PDF)",
            data=pdf_data,
            file_name=f"ScolioAI_Report_{st.session_state['filename']}.pdf",
            mime="application/pdf"
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
