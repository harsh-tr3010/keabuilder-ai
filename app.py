import streamlit as st

st.set_page_config(
    page_title="KeaBuilder AI",
    layout="wide"
)

st.sidebar.title("🚀 KeaBuilder AI")

page = st.sidebar.radio(
    "Navigation",
    [
    "Dashboard",
    "Lead AI",
    "Content Router",
    "AI Brand Images",
    "Similarity Search",
    "Reliability",
    "Queue System"
]
)

if page == "Dashboard":
    st.title("KeaBuilder AI Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric("Leads Today", "124")
    c2.metric("AI Outputs", "58")
    c3.metric("Success Rate", "98%")

    st.info("Use sidebar to test modules.")


elif page == "Lead AI":
    from services.lead_engine import classify_lead, generate_human_reply

    st.title("Lead Intelligence")

    name = st.text_input("Full Name")
    budget = st.number_input("Budget", 0, 100000, 3000)
    urgency = st.selectbox("Urgency", ["High", "Medium", "Low"])
    message = st.text_area("What does the lead need?")

    if st.button("Analyze Lead"):

        if not name or not message:
            st.warning("Please fill required fields.")
        else:
            result = classify_lead(name, budget, urgency, message)

            st.subheader("Lead Output")
            st.json(result)

            reply = generate_human_reply(
                name,
                result["tier"],
                message
            )

            st.subheader("AI Response")
            st.success(reply)
elif page == "Content Router":

    from services.content_router import route_request

    st.title("AI Content Router")

    content_type = st.selectbox(
        "Select Content Type",
        ["Image", "Video", "Voice"]
    )

    prompt = st.text_area("Enter Prompt")

    if st.button("Generate Content"):

        if not prompt:
            st.warning("Please enter prompt.")
        else:
            with st.spinner("Generating..."):
                result = route_request(content_type, prompt)

            st.subheader("Generation Output")
            st.json(result)

            st.success("Request completed successfully.")
elif page == "AI Brand Images":

    from services.image_generator import generate_lora_image

    st.title("Brand Consistent AI Images")

    brand = st.text_input("Brand Name")
    uploaded = st.file_uploader(
        "Upload logo / face reference",
        type=["png", "jpg", "jpeg"]
    )

    prompt = st.text_area("Prompt")

    if st.button("Generate Brand Image"):

        if not brand or not prompt:
            st.warning("Please complete fields.")
        else:
            with st.spinner("Generating..."):

                result = generate_lora_image(
                    brand,
                    prompt
                )

            st.subheader("Output")
            st.json(result)

            st.success("Brand image generated.")
elif page == "Similarity Search":

    from services.embedding_search import semantic_search

    st.title("AI Similarity Search")

    query = st.text_input(
        "Search assets/templates"
    )

    if st.button("Find Similar"):

        if not query:
            st.warning("Enter query")
        else:
            result = semantic_search(query)

            st.subheader("Results")
            st.json(result)
elif page == "Reliability":

    from services.fallback_manager import generate_with_fallback

    st.title("AI Reliability System")

    prompt = st.text_area("Prompt")

    if st.button("Run Safe Request"):

        result = generate_with_fallback(prompt)

        st.json(result)            
else:

    from services.queue_manager import add_job, process_jobs

    st.title("High Volume Queue System")

    job_type = st.selectbox(
        "Job Type",
        ["Image", "Video", "Voice"]
    )

    prompt = st.text_input("Prompt")

    if st.button("Add Job"):
        job_id = add_job(job_type, prompt)
        st.success(f"Job Added: {job_id}")

    if st.button("Process Queue"):
        result = process_jobs()
        st.json(result)