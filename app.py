import streamlit as st
from config import APP_NAME, APP_TAGLINE

st.set_page_config(
    page_title=APP_NAME,
    layout="wide",
    page_icon="🚀",
    initial_sidebar_state="expanded"
)

st.title(APP_NAME)
st.caption(APP_TAGLINE)

st.sidebar.title("KeaBuilder Workspace")
st.sidebar.success("AI Assessment Build")
st.sidebar.caption("Dream Reflection Media")

st.markdown("""
## Welcome to KeaBuilder AI Engine

An AI-powered SaaS prototype designed for:

- Funnel Building  
- Lead Capture  
- Content Generation  
- Automation Workflows  
- Reliability & Scaling  
- Asset Intelligence  

---

## What This Demo Shows

This project demonstrates how AI can be embedded inside a SaaS platform like KeaBuilder to improve growth workflows and user productivity.

### Core Modules

- **Dashboard** → Usage metrics & system overview  
- **Lead AI** → Classify Hot / Warm / Cold leads + AI replies  
- **Content Router** → Route Images / Videos / Voice to best providers  
- **LoRA Brand Images** → Personalized AI visuals with consistent identity  
- **Similarity Search** → Find related templates / assets  
- **Reliability Center** → Fallback handling & provider resilience  
- **Scale Engine** → High-volume architecture simulation  
- **Admin Analytics** → Operational insights  

---

## How to Navigate

Use the **left sidebar** to open any module.

## Tech Stack

- Streamlit  
- Python  
- Groq API  
- Modular SaaS Architecture  

---

## Goal

To showcase practical AI product engineering, system design, and execution clarity.
""")