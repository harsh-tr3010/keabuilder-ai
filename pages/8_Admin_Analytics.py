import streamlit as st
import pandas as pd

st.title("Admin Analytics")

df = pd.DataFrame({
    "Module": ["Lead AI", "Content", "Automation", "Search"],
    "Usage": [420, 310, 220, 190]
})

st.bar_chart(df.set_index("Module"))