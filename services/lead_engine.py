import json
from services.groq_service import ask_groq


def calculate_score(budget, urgency, message):
    score = 0
    msg = message.lower()

    # Budget
    if budget >= 10000:
        score += 40
    elif budget >= 5000:
        score += 30
    elif budget >= 2000:
        score += 20
    else:
        score += 10

    # Urgency
    if urgency == "High":
        score += 30
    elif urgency == "Medium":
        score += 20
    else:
        score += 10

    # Intent keywords
    hot_words = ["urgent", "today", "now", "ready", "buy", "asap"]
    warm_words = ["price", "pricing", "details", "demo", "plan"]

    if any(word in msg for word in hot_words):
        score += 20
    elif any(word in msg for word in warm_words):
        score += 10

    return min(score, 100)


def get_tier(score):
    if score >= 75:
        return "Hot"
    elif score >= 45:
        return "Warm"
    return "Cold"


def get_next_action(tier):
    if tier == "Hot":
        return "Immediate sales callback"
    elif tier == "Warm":
        return "Send pricing and schedule follow-up"
    return "Add to nurture email sequence"


def classify_lead(name, budget, urgency, message):
    score = calculate_score(budget, urgency, message)
    tier = get_tier(score)

    return {
        "name": name,
        "budget": budget,
        "urgency": urgency,
        "message": message,
        "score": score,
        "tier": tier,
        "next_action": get_next_action(tier)
    }


def generate_human_reply(name, tier, message):
    prompt = f"""
You are a friendly SaaS sales assistant.

Write a short personalized response.

Lead Name: {name}
Lead Tier: {tier}
Lead Message: {message}

Rules:
- Sound human
- Warm and professional
- Max 60 words
"""

    result = ask_groq(prompt)

    if result.startswith("ERROR"):
        return f"Hi {name}, thanks for reaching out. Our team will contact you shortly."

    return result