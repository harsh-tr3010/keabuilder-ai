def route_task(task):
    if task == "Image":
        return "Replicate"
    if task == "Video":
        return "Runway"
    if task == "Voice":
        return "ElevenLabs"
    return "Groq"