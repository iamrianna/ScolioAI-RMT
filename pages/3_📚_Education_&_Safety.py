import streamlit as st

st.header("Scoliosis Clinical Background & AI Safety")

st.markdown("""
<div style="background-color: #FFFFFF; border-radius: 12px; padding: 24px; border: 1px solid #E2E8F0; margin-bottom: 20px;">
    <h3>Understanding Scoliosis Assessment</h3>
    <p>Scoliosis is a three-dimensional spinal deformity defined as a lateral curvature of the spine in the frontal plane of <b>10 degrees or greater</b>, measured via the Cobb angle method on standing radiographs.</p>
    
    <h4>What Image Classifiers CAN Do:</h4>
    <ul>
        <li>Identify global structural pattern asymmetries in full-spine radiographs.</li>
        <li>Screen for features prompting referral to specialist orthopedic evaluation.</li>
        <li>Accelerate clinical triage workflows in high-volume settings.</li>
    </ul>

    <h4>What Image Classifiers CANNOT Do:</h4>
    <ul>
        <li>A standard 2D classification CNN <b>cannot calculate an accurate Cobb angle</b>.</li>
        <li>Cannot replace a physician's physical exam, vertebral rotation check, or Risser staging.</li>
        <li>Cannot serve as a stand-alone diagnostic system without clinical validation and regulatory authorization.</li>
    </ul>
</div>
""", unsafe_allow_html=True)
