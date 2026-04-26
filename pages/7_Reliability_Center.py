import streamlit as st
from core.fallback import provider_with_fallback

st.title("Reliability Center")

sample = st.selectbox("Simulate Result", ["success", "error timeout"])

if st.button("Check"):
    st.write(provider_with_fallback(sample))