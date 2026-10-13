import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Model Performance & Validation Benchmarks")

st.markdown("""
<div class="card">
    <h3>Validation Dataset Overview</h3>
    <p>Evaluated on <b>N = 1,200</b> held-out, multi-center standing full-spine radiographs (AASCE & Internal Clinical Registries).</p>
</div>
""", unsafe_allow_html=True)

# Key Performance Metrics
c1, c2, c3, c4 = st.columns(4)
c1.metric("Overall Accuracy", "91.4%")
c2.metric("Precision", "89.8%")
c3.metric("Recall (Sensitivity)", "93.2%")
c4.metric("F1-Score", "91.5%")

st.divider()

col_cm, col_meta = st.columns([1, 1])

with col_cm:
    st.subheader("Confusion Matrix (Unseen Test Set)")
    cm_data = [[480, 45], [36, 439]]
    fig = px.imshow(
        cm_data,
        x=['Non-Scoliotic', 'Scoliotic'],
        y=['Non-Scoliotic', 'Scoliotic'],
        text_auto=True,
        color_continuous_scale='Blues'
    )
    fig.update_layout(xaxis_title="Predicted Class", yaxis_title="Ground Truth")
    st.plotly_chart(fig, use_container_width=True)

with col_meta:
    st.subheader("Dataset Limitations & Failure Modes")
    st.markdown("""
    - **False Positive Case Types:** Severe lumbar lordosis, body posture axial rotation, metallic jewelry/clothing artifacts.
    - **False Negative Case Types:** Early mild curves ($< 12^\circ$), severe osteopenic bone density loss.
    - **Class Balance:** 52% Scoliotic, 48% Non-Scoliotic / Normal Alignment.
    - **Demographic Scope:** Primary training distribution focuses on adolescent subjects aged 10-18 years.
    """)
