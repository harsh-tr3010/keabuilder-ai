def route_content(kind):
    providers = {
        "Image":"Stability AI",
        "Video":"Runway",
        "Voice":"ElevenLabs"
    }
    return providers.get(kind,"Unknown")
