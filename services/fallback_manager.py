from services.groq_service import ask_groq


def generate_with_fallback(prompt):
    """
    Try main AI model first.
    If fail -> fallback response.
    """

    result = ask_groq(prompt)

    if result.startswith("ERROR"):
        return {
            "provider": "Fallback Engine",
            "status": "backup_used",
            "response": "Our AI service is busy right now. We’ll process your request shortly."
        }

    return {
        "provider": "Groq",
        "status": "success",
        "response": result
    }