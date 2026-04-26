def score_lead(budget, timeline, need):
    score = 0

    if budget >= 1000:
        score += 40
    elif budget >= 500:
        score += 25
    else:
        score += 10

    if timeline == "Immediate":
        score += 30
    elif timeline == "This Month":
        score += 20

    if len(need) > 20:
        score += 20

    return min(score, 100)

def classify(score):
    if score >= 70:
        return "Hot"
    elif score >= 40:
        return "Warm"
    return "Cold"