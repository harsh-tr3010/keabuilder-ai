def run_rule(label):
    if label == "Hot":
        return "Notify sales team instantly"
    elif label == "Warm":
        return "Send nurture email sequence"
    return "Add to long-term campaign"