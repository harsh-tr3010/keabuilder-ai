import streamlit as st
from services.lead_engine import classify_lead, generate_reply
from services.router import route_content
from services.search_engine import search_assets
from services.image_generator import generate_image
from services.video_generator import generate_video
from services.voice_generator import generate_voice
from services.embedding_search import semantic_search
from services.job_queue import queue_job

st.set_page_config(page_title="KeaBuilder AI", layout="wide")

st.sidebar.title("🚀 KeaBuilder AI")
menu = st.sidebar.radio("Menu", [
    "Dashboard",
    "Lead AI",
    "Image Generator",
    "Video Generator",
    "Voice Generator",
    "Similarity Search",
    "Queue System"
])

if menu == "Dashboard":
    st.title("KeaBuilder AI SaaS Dashboard")
    c1,c2,c3 = st.columns(3)
    c1.metric("Leads", "124")
    c2.metric("Outputs", "58")
    c3.metric("Success", "98%")

elif menu == "Lead AI":
    st.title("Lead Classification")

    name = st.text_input("Name")
    budget = st.number_input("Budget", 0, 100000, 1000)
    urgency = st.selectbox("Urgency", ["High","Medium","Low"])
    msg = st.text_area("Message")

    if st.button("Process Lead"):
        data = classify_lead(name,budget,urgency,msg)
        st.json(data)
        st.success(generate_reply(name,data["tier"],msg))

elif menu == "Image Generator":
    st.title("AI Image Generator")
    prompt = st.text_input("Image Prompt")

    if st.button("Generate Image"):
        st.success(generate_image(prompt))

elif menu == "Video Generator":
    st.title("AI Video Generator")
    prompt = st.text_input("Video Prompt")

    if st.button("Generate Video"):
        st.success(generate_video(prompt))

elif menu == "Voice Generator":
    st.title("AI Voice Generator")
    text = st.text_area("Text")

    if st.button("Generate Voice"):
        st.success(generate_voice(text))

elif menu == "Similarity Search":
    st.title("Semantic Search")
    q = st.text_input("Search")

    if st.button("Find"):
        st.json(semantic_search(q))

else:
    st.title("High Volume Queue")
    task = st.text_input("Task")

    if st.button("Add Queue"):
        st.success(queue_job(task))
