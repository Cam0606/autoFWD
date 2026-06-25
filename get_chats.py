import os

from dotenv import load_dotenv
from telethon.sync import TelegramClient

# --- Load config ---
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# --- List all dialogs (channels, groups, private chats) ---
# Run this script once to find the ID of your destination channel,
# then copy it into DEST_CHANNEL in your .env file.
with TelegramClient("autofwd", API_ID, API_HASH) as client:
    print(f"{'ID':>15} | {'Type':<10} | Name")
    print("-" * 70)
    for dialog in client.iter_dialogs():
        entity_type = type(dialog.entity).__name__
        print(f"{dialog.id:>15} | {entity_type:<10} | {dialog.name}")