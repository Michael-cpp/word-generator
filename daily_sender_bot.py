from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
from utils import pop_random_word, load_users

import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)

def send_daily_word():
    word = pop_random_word()
    if not word:
        return
    for chat_id in load_users():
        try:
            bot.send_message(chat_id=chat_id, text=word)
        except Exception as e:
            print(f"Failed to send to {chat_id}: {e}")

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(send_daily_word, 'cron', hour=9)  # e.g., 9 AM daily
    print("Daily sender started...")
    scheduler.start()
