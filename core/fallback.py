def provider_with_fallback(primary_result):
    if "error" in str(primary_result).lower():
        return "Fallback activated: Rule Engine"
    return "Primary provider successful"