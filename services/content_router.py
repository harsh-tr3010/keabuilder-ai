import time
import uuid


def route_request(content_type, prompt):
    providers = {
        "Image": "Stability AI",
        "Video": "Runway ML",
        "Voice": "ElevenLabs"
    }

    provider = providers.get(content_type, "Unknown")

    job_id = str(uuid.uuid4())[:8]

    time.sleep(1)

    return {
        "job_id": job_id,
        "type": content_type,
        "provider": provider,
        "prompt": prompt,
        "status": "completed",
        "output_url": f"https://keabuilder.ai/output/{job_id}"
    }