import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
    SESSION_HOURS = int(os.getenv("SESSION_HOURS", 24))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
