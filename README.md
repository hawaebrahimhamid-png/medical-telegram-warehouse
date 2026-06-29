# medical-telegram-warehouse
Task 1 – Telegram Data Scraping & Validation (RAG Complaint Chatbot)
📖 Overview

This project is part of the RAG-Powered Complaint Analysis System.

Task 1 focuses on:

Connecting to Telegram using Telethon
Scraping messages from selected channels
Extracting structured data
Downloading media (images)
Saving data in JSON format
Performing basic validation checks
🎯 Objectives
Authenticate Telegram API connection
Extract messages from public channels
Collect structured metadata (text, views, forwards, etc.)
Download images attached to messages
Store data in organized folder structure
Validate extracted dataset
📁 Project Structure
rag-complaint-chatbot/
│
├── data/
│   └── raw/
│       ├── telegram_messages/
│       │   └── 2026-06-29/
│       │       ├── lobelia4cosmetics.json
│       │       └── tikvahpharma.json
│       │
│       └── images/
│           ├── lobelia4cosmetics/
│           └── tikvahpharma/
│
├── logs/
│   └── scraper.log
│
├── src/
│   └── scraper.py
│
├── .env
├── requirements.txt
└── README.md
⚙️ Installation
1. Clone repository
git clone https://github.com/your-username/rag-complaint-chatbot.git
cd rag-complaint-chatbot
2. Create virtual environment
python -m venv .venv
3. Activate environment

Windows:

.venv\Scripts\activate

Mac/Linux:

source .venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the root directory:

API_ID=your_api_id
API_HASH=your_api_hash

These credentials are required to access the Telegram API via Telethon.

🚀 How to Run

Run the scraper using:

python src/scraper.py
🔄 What the Script Does
📡 1. Connects to Telegram

Uses:

Telethon TelegramClient
.env credentials (API_ID, API_HASH)
📥 2. Scrapes Channels

Configured channels:

lobelia4cosmetics
tikvahpharma

Extracts:

message ID
message text
message date
views
forwards
media presence
🖼️ 3. Downloads Media

If a message contains an image:

Image is downloaded into:
data/raw/images/<channel_name>/

Format:

message_id.jpg
💾 4. Saves Structured Data

Each channel is saved as JSON:

data/raw/telegram_messages/<date>/<channel>.json

Example structure:

{
  "message_id": 123,
  "channel_name": "lobelia4cosmetics",
  "message_date": "2026-06-29T10:30:00",
  "message_text": "Paracetamol 500mg",
  "views": 120,
  "forwards": 5,
  "has_media": true
}
✅ 5. Validation Step

After scraping, the script verifies:

Required fields exist:
message_id
message_date
message_text
views
forwards

Output:

STEP 2 VALIDATION:
True
🛠️ Technologies Used
Python 3.10+
Telethon (Telegram API)
python-dotenv
JSON
asyncio
logging
📊 Logging

All execution logs are stored in:

logs/scraper.log

Logs include:

Scraping start/end
Channel progress
Errors
Media download status
📌 Notes
Do NOT upload .env file to GitHub
Ensure API credentials are valid
Data is automatically organized by date
Only public channels are supported
