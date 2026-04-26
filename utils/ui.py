import streamlit as st

def metric_row(a, b, c):
    col1, col2, col3 = st.columns(3)
    col1.metric(a[0], a[1])
    col2.metric(b[0], b[1])
    col3.metric(c[0], c[1])