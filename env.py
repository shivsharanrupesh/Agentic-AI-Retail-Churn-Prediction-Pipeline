# env.py
import os
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

# Required environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY must be set in the environment or .env file.")
