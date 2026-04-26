import streamlit as st
from core.similarity_engine import find_matches

st.title("Similarity Search")

query = st.text_input("Search similar templates")

if st.button("Search"):
    results = find_matches(query)
    for r in results:
        st.write("-", r)