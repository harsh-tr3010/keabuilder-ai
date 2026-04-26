import uuid
import time


queue = []


def add_job(job_type, prompt):
    job_id = str(uuid.uuid4())[:8]

    queue.append({
        "job_id": job_id,
        "type": job_type,
        "prompt": prompt,
        "status": "queued"
    })

    return job_id


def process_jobs():
    completed = []

    for item in queue:
        time.sleep(0.5)

        item["status"] = "completed"
        completed.append(item)

    return completed