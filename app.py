import streamlit as st
from config import APP_NAME, APP_TAGLINE

st.set_page_config(
    page_title=APP_NAME,
    layout="wide",
    page_icon="🚀"
)

st.title(APP_NAME)
st.caption(APP_TAGLINE)

st.markdown(
"""
### Welcome

This is a demo AI suite designed for a funnel / lead capture / automation SaaS platform.

Use the left sidebar to open modules:

- Dashboard
- Lead AI
- Content Generator
- Funnel Copilot
- Automation AI
- Similarity Search
- Reliability Center
- Admin Analytics
"""
)