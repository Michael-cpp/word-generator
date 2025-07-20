from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils import pop_random_word, load_users

import os
import asyncio

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)

async def send_daily_word():
    word = pop_random_word()
    if not word:
        print("No word to send.")
        return

    users = load_users()
    print(f"Loaded users: {users}")
    for chat_id in users:
        try:
            await bot.send_message(chat_id=chat_id, text=word)
            print(f"Sent word to {chat_id}")
        except Exception as e:
            print(f"Failed to send to {chat_id}: {e}")

async def main():
    print("Starting daily word scheduler...")
    
    # Initialize scheduler
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_daily_word, 'cron', hour=9)
    scheduler.start()

    # Run the event loop
    await asyncio.Event().wait()  # This keeps the loop running indefinitely

if __name__ == '__main__':
    asyncio.run(main())
