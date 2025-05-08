import os
from dotenv import load_dotenv
load_dotenv()
HUMANDESIGN_API_KEY = os.getenv("HUMANDESIGN_API_KEY")

MAX_API_CALLS = int(os.getenv("HUMANDESIGN_MAX_CALLS", 950))
