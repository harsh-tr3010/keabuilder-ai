from services.groq_service import ask_groq

def generate_copy(goal):
    prompt = f"Write landing page headline, CTA and short body copy for {goal}"
    return ask_groq(prompt)