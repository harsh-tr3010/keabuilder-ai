from groq import Groq
from config import Config

client = Groq(api_key=Config.GROQ_API_KEY)

def ask_groq(prompt, temperature=0.4):
    try:
        response = client.chat.completions.create(
            model=Config.MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"ERROR: {str(e)}"