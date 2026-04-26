def missing_fields(data: dict):
    missing = []
    for k, v in data.items():
        if str(v).strip() == "":
            missing.append(k)
    return missing