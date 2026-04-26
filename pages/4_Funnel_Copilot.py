import streamlit as st
from core.funnel_engine import recommend_funnel

st.title("Funnel Copilot")

industry = st.selectbox("Industry", ["Real Estate", "Fitness", "Ecommerce", "Other"])

if st.button("Recommend Funnel"):
    st.success(recommend_funnel(industry))