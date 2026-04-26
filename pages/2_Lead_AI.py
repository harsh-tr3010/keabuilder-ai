import streamlit as st
from core.lead_engine import score_lead, classify
from core.response_engine import personalized_reply

st.title("Lead AI")

name = st.text_input("Name")
budget = st.number_input("Budget", 0, 100000, 500)
timeline = st.selectbox("Timeline", ["Immediate", "This Month", "Later"])
need = st.text_area("Requirement")

if st.button("Process Lead"):
    score = score_lead(budget, timeline, need)
    label = classify(score)
    reply = personalized_reply(name, need, label)

    st.success(f"{label} Lead | Score: {score}")
    st.write(reply)