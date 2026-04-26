import streamlit as st
from core.content_engine import generate_copy

st.title("Content Generator")

goal = st.text_input("What are you promoting?")

if st.button("Generate"):
    st.write(generate_copy(goal))