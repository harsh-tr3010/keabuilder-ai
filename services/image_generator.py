import uuid
import time


def generate_lora_image(brand_name, prompt):
    """
    Simulated LoRA image generation flow
    """

    model_used = f"{brand_name.lower()}_lora.safetensors"

    job_id = str(uuid.uuid4())[:8]

    time.sleep(1)

    return {
        "job_id": job_id,
        "model": model_used,
        "status": "completed",
        "prompt": prompt,
        "image_url": f"https://keabuilder.ai/images/{job_id}.png"
    }