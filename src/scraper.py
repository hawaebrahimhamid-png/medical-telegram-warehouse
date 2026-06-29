import logging
import json
from datetime import datetime
from telethon import TelegramClient
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

# Logging
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("telegram_session", api_id, api_hash)

channels = [
    "lobelia4cosmetics",
    "tikvahpharma"
]

async def main():
    logging.info("Scraping started")

    all_messages = {}

    today = datetime.now().strftime("%Y-%m-%d")

    json_dir = f"data/raw/telegram_messages/{today}"
    os.makedirs(json_dir, exist_ok=True)

    for channel in channels:
        try:
            logging.info(f"Scraping channel: {channel}")
            print(f"\nScraping {channel}")

            messages = []

            image_dir = f"data/raw/images/{channel}"
            os.makedirs(image_dir, exist_ok=True)

            async for message in client.iter_messages(channel, limit=5):

                data = {
                    "message_id": message.id,
                    "channel_name": channel,
                    "message_date": message.date.isoformat(),
                    "message_text": message.text or "",
                    "views": message.views or 0,
                    "forwards": message.forwards or 0,
                    "has_media": message.photo is not None
                }

                messages.append(data)

                if message.photo:
                    path = f"{image_dir}/{message.id}.jpg"
                    await client.download_media(message, file=path)

                    logging.info(f"Downloaded image for message {message.id}")
                    print("IMAGE SAVED:", path)

            all_messages[channel] = messages

            json_path = f"{json_dir}/{channel}.json"

            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(messages, f, ensure_ascii=False, indent=2)

            logging.info(f"Saved {len(messages)} messages from {channel}")
            print(f"Saved {len(messages)} messages to {json_path}")

        except Exception as e:
            logging.error(f"Error scraping {channel}: {str(e)}")
            print(f"Error scraping {channel}: {e}")

    # ✅ SAFE VALIDATION
    print("\nSTEP 2 VALIDATION:")

    if all_messages:
        first_channel = list(all_messages.keys())[0]

        if all_messages[first_channel]:
            sample = all_messages[first_channel][0]

            required_fields = [
                "message_id",
                "message_date",
                "message_text",
                "views",
                "forwards"
            ]

            print(all(field in sample for field in required_fields))
        else:
            print("No messages found in first channel")
    else:
        print("No data scraped at all")


with client:
    client.loop.run_until_complete(main())
