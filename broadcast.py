import argparse
import asyncio
import os

from telegram import Bot
from utils import load_users

BOT_TOKEN = os.getenv('BOT_TOKEN')


async def broadcast(text: str, chat_ids: list[int]):
    async with Bot(token=BOT_TOKEN) as bot:
        for chat_id in chat_ids:
            try:
                await bot.send_message(chat_id=chat_id, text=text)
                print(f"Sent to {chat_id}")
            except Exception as e:
                print(f"Failed to send to {chat_id}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Send a message to the bot's users.")
    parser.add_argument('text', help="message text")
    parser.add_argument('--to', type=int, action='append', metavar='CHAT_ID',
                        help="send only to this chat (repeatable), e.g. to test")
    parser.add_argument('--dry-run', action='store_true',
                        help="print the recipients and the text without sending")
    args = parser.parse_args()

    chat_ids = args.to or load_users()
    if not chat_ids:
        print("No recipients.")
        return

    print(f"Recipients ({len(chat_ids)}): {chat_ids}")
    print(f"Text:\n{args.text}")
    if args.dry_run:
        return

    asyncio.run(broadcast(args.text, chat_ids))


if __name__ == '__main__':
    main()
