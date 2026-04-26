import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "KeaBuilder AI Engine"
APP_TAGLINE = "Lead Intelligence • Content Automation • Smart SaaS AI"

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")

DATA_DIR = "data"
ASSET_DIR = "assets"

PRIMARY_TEXT_PROVIDER = "Groq"
BACKUP_TEXT_PROVIDER = "Rule Engine"

IMAGE_PROVIDER = "Replicate"
VIDEO_PROVIDER = "Runway"
VOICE_PROVIDER = "ElevenLabs"