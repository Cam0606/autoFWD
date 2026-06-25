import os
import logging
import random
import asyncio

from dotenv import load_dotenv
from telethon import TelegramClient, events


# --- Logs config ---
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("autofwd")

# --- Load config ---
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")
DEST_CHANNEL = int(os.getenv("DEST_CHANNEL"))

DELAY_MIN = 5
DELAY_MAX = 20

# --- Initialize Telethon client ---
client = TelegramClient("autofwd", API_ID, API_HASH)


@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    """Triggered on every new message from the source channel."""
    message = event.message

    # Random delay to avoid detection
    delay = random.uniform(DELAY_MIN, DELAY_MAX)
    logger.info(f"New message received (id={message.id}), waiting {delay:.1f}s before reposting")
    await asyncio.sleep(delay)

    try:
        if message.media:
            # Media with or without caption
            await client.send_file(
                DEST_CHANNEL,
                file=message.media,
                caption=message.text or "",
            )
            logger.info(f"Media reposted (id={message.id})")

        elif message.text:
            # Plain text message
            await client.send_message(DEST_CHANNEL, message.text)
            logger.info(f"Text reposted (id={message.id})")

        else:
            logger.warning(f"Message id={message.id} skipped (no text or media)")

    except Exception as e:
        logger.error(f"Failed to repost message id={message.id}: {e}")


def main():
    logger.info("Starting autoFWD bot")
    logger.info(f"Source channel: {SOURCE_CHANNEL}")
    logger.info(f"Destination channel: {DEST_CHANNEL}")
    client.start()
    logger.info("Connected to Telegram, waiting for messages...")
    client.run_until_disconnected()


if __name__ == "__main__":
    main()