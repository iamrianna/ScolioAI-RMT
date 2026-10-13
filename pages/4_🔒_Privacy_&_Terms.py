import streamlit as st

st.header("Data Privacy & Responsible Use Guidelines")

st.markdown("""
<div class="card">
    <h3>Data Privacy Assurance</h3>
    <p>Scolio-AI processes uploaded files strictly within runtime memory (RAM) during your active browser session:</p>
    <ul>
        <li>Uploaded DICOM/image files are <b>never saved or written to permanent storage</b>.</li>
        <li>DICOM header fields are parsed to strip metadata before generating PDF outputs.</li>
        <li>All session state data automatically purges when the browser tab is closed.</li>
    </ul>

    <h3>Responsible AI Framework</h3>
    <p>This software is provided purely as an academic research demonstrator. It has not been cleared by the FDA or CE-marked as a medical device.</p>
</div>
""", unsafe_allow_html=True)
