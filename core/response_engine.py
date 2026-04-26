from services.groq_service import ask_groq

def personalized_reply(name, need, label):
    prompt = f"""
    Write a short professional sales response.
    Customer name: {name}
    Need: {need}
    Lead type: {label}
    """
    return ask_groq(prompt)