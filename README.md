# autoFWD

Automatically forwards messages from a public Telegram channel to a private destination channel — in real time, 24/7.

Built with [Telethon](https://docs.telethon.dev/) (MTProto), which means it works even when you're not an admin of the source channel.

---

## How it works

The script runs a dedicated Telegram account that is subscribed to the source channel. Every time a new message is posted — text, image, or image with caption — it gets copied to the destination channel within a few seconds. Messages appear natively, with no source attribution.

A random delay is introduced between each forward to reduce detection risk.

---

## Requirements

- Python 3.10+
- A secondary Telegram account (recommended)
- Telegram API credentials from [my.telegram.org](https://my.telegram.org)
- The secondary account must be: subscribed to the source channel, and added to the destination channel with posting rights

---

## Setup

**1. Clone the repo**

```bash
git clone https://github.com/Cam0606/autoFWD.git
cd autoFWD
```

**2. Install dependencies**

```bash
pip install telethon python-dotenv
```

**3. Configure your credentials**

```bash
cp .env.example .env
```

Then fill in your `.env`:

```
API_ID=your_api_id
API_HASH=your_api_hash
SOURCE_CHANNEL=@source_channel_username
DEST_CHANNEL=-100xxxxxxxxxx
```

To find the numeric ID of your private destination channel, run:

```bash
python get_chats.py
```

This lists all channels and groups accessible from your account with their IDs.

**4. Run**

```bash
python autofwd.py
```

On first run, Telethon will ask for your phone number and a verification code. A `.session` file is then saved locally — subsequent runs are fully automatic.

---

## Deployment (VPS)

For 24/7 operation, deploy on a Linux VPS (e.g. [Hetzner CX22](https://www.hetzner.com/cloud), ~€4/month).

Transfer your files and `.session` to the server, then set up a systemd service so the bot starts automatically on boot and restarts on crash.

---

## Project structure

```
autoFWD/
├── autofwd.py        # main script
├── get_chats.py      # one-time utility to list channel IDs
├── .env              # your credentials (never commit this)
├── .env.example      # template
├── autofwd.session   # your Telegram session (never commit this)
├── README.md         # all informations you need !
└── .gitignore
```

---

## Security

- Never commit `.env` or `*.session` files — they contain your Telegram credentials
- Run the bot on a dedicated secondary account, not your personal one
- `API_ID`, `API_HASH`, and the `.session` file together give full access to the Telegram account

---

## License

This project is open source — free to use, modify, and distribute.