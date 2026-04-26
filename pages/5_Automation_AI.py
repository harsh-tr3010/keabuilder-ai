import streamlit as st
from core.automation_engine import run_rule

st.title("Automation AI")

lead = st.selectbox("Lead Type", ["Hot", "Warm", "Cold"])

if st.button("Run Workflow"):
    st.info(run_rule(lead))