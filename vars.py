import os

API_ID    = os.environ.get("API_ID", "27900743")
API_HASH  = os.environ.get("API_HASH", "ebb06ea8d41420e60b29140dcee902fc")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7857589413:AAE79aTmwa6-LIdbK0L4xS1byZJQIH2IR8U") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
