# backend/config.py

import os
from dotenv import load_dotenv

load_dotenv()

# === Human Design ===
HUMANDESIGN_API_KEY = os.getenv("HUMANDESIGN_API_KEY")
MAX_API_CALLS = int(os.getenv("HUMANDESIGN_MAX_CALLS", 950))

# === MongoDB ===
MONGO_URI = os.getenv("MONGO_URI")

# === Redis ===
REDIS_URL = os.getenv("REDIS_URL")
