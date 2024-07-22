import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    print("Loaded .env file from:", dotenv_path)
else:
    print(".env file not found at:", dotenv_path)


BLASTSCAN_API_KEY = os.getenv("BLASTSCAN_API_KEY")
assert isinstance(BLASTSCAN_API_KEY, str), "BLASTSCAN_API_KEY not found"

DISCORD_CLIENT_TOKEN = os.getenv("DISCORD_CLIENT_TOKEN")
assert isinstance(DISCORD_CLIENT_TOKEN, str), "DISCORD_CLIENT_TOKEN not found"

QUIT_CHANNEL_ID = os.getenv("QUIT_CHANNEL_ID")
assert isinstance(QUIT_CHANNEL_ID, str), "QUIT_CHANNEL_ID not found"
QUIT_CHANNEL_ID = int(QUIT_CHANNEL_ID)
print(f"Using channel for quit price: {QUIT_CHANNEL_ID}")


QR_CHANNEL_ID = os.getenv("QR_CHANNEL_ID")
assert isinstance(QR_CHANNEL_ID, str), "QR_CHANNEL_ID not found"
QR_CHANNEL_ID = int(QR_CHANNEL_ID)
print(f"Using channel for quit + royalties price: {QR_CHANNEL_ID}")

CATEGORY = os.getenv("CATEGORY")
assert isinstance(CATEGORY, str), "CATEGORY not found"
CATEGORY = int(CATEGORY)
print(f"Using category: {CATEGORY}")