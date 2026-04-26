import streamlit as st
from core.router import route_task

st.title("Multi-Provider Content Router")

st.write("Generate Images, Videos, or Voice using specialized providers.")

task = st.selectbox(
    "Select Content Type",
    ["Image", "Video", "Voice"]
)

prompt = st.text_area(
    "Enter Prompt",
    placeholder="Example: Modern gym ad creative"
)

quality = st.selectbox(
    "Priority",
    ["Fast", "Balanced", "Premium"]
)

if st.button("Generate Content"):
    provider = route_task(task)

    st.success(f"Request Routed To: {provider}")

    st.code(f"""
POST /api/generate
{{
  "type": "{task.lower()}",
  "prompt": "{prompt}",
  "priority": "{quality.lower()}"
}}
""")

    st.info("Frontend sends one request. Backend routes to best provider.")

    if task == "Image":
        st.image("assets/demo_outputs/generated_image.png")

    elif task == "Video":
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")

    else:
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

    st.json({
        "type": task,
        "provider": provider,
        "status": "completed",
        "saved_to": "workspace_assets/"
    })