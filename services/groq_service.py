from groq import Groq
from config import Config

client = Groq(api_key=Config.GROQ_API_KEY)

def ask_groq(prompt):
    try:
        res = client.chat.completions.create(
            model=Config.MODEL,
            messages=[{"role":"user","content":prompt}],
            temperature=0.5
        )
        return res.choices[0].message.content
    except:
        return "AI response unavailable"
