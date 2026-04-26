import streamlit as st
from core.analytics_engine import dashboard_stats

st.title("Dashboard")

stats = dashboard_stats()

c1, c2, c3 = st.columns(3)
c1.metric("Requests", stats["requests"])
c2.metric("Success Rate", stats["success_rate"])
c3.metric("Fallbacks", stats["fallbacks"])