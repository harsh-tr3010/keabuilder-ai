from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

client = None

if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)

def ask_groq(prompt, temperature=0.3):
    if client is None:
        return "Groq key missing. Using offline mode."

    try:
        res = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Provider error: {str(e)}"