import json
from services.groq_service import ask_groq


def rule_score(budget, urgency, msg):
    score = 0
    msg = msg.lower()

    # Budget score
    if budget >= 10000:
        score += 40
    elif budget >= 5000:
        score += 30
    elif budget >= 2000:
        score += 20
    else:
        score += 10

    # Urgency score
    if urgency == "High":
        score += 30
    elif urgency == "Medium":
        score += 20
    else:
        score += 10

    # Intent keywords
    hot_words = [
        "today", "urgent", "asap", "now",
        "ready", "buy", "start", "demo"
    ]

    warm_words = [
        "pricing", "price", "cost",
        "details", "options", "plan"
    ]

    for word in hot_words:
        if word in msg:
            score += 20
            break

    for word in warm_words:
        if word in msg:
            score += 10
            break

    return min(score, 100)


def get_tier(score):
    if score >= 75:
        return "Hot"
    elif score >= 45:
        return "Warm"
    return "Cold"


def next_action(tier):
    if tier == "Hot":
        return "Call immediately and assign sales rep."
    elif tier == "Warm":
        return "Send pricing + schedule follow-up."
    return "Add to nurture email campaign."


def classify_lead(name, budget, urgency, msg):
    score = rule_score(budget, urgency, msg)
    tier = get_tier(score)

    return {
        "name": name,
        "budget": budget,
        "urgency": urgency,
        "message": msg,
        "score": score,
        "tier": tier,
        "next_action": next_action(tier)
    }


def classify_lead_ai(name, budget, urgency, msg):
    prompt = f"""
You are a lead scoring AI.

Classify this lead as Hot, Warm, or Cold.

Return JSON only:

{{
"name":"",
"score":0,
"tier":"",
"reason":"",
"next_action":""
}}

Lead Data:
Name: {name}
Budget: {budget}
Urgency: {urgency}
Message: {msg}
"""

    try:
        result = ask_groq(prompt)
        return json.loads(result)
    except:
        return classify_lead(name, budget, urgency, msg)


def generate_reply(name, tier, msg):
    if tier == "Hot":
        return f"Hi {name}, thanks for reaching out. We’re prioritizing your request and will contact you shortly."

    elif tier == "Warm":
        return f"Hi {name}, thank you for your interest. We’ll share the best options and pricing soon."

    return f"Hi {name}, thanks for contacting us. We’ll send helpful details shortly."