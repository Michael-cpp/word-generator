from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from utils import get_word_message, load_users

import os

BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id not in load_users():
        return

    keyboard = [[InlineKeyboardButton("Generate", callback_data='generate')]]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Welcome! Click 'Generate' to learn a new word.",
        reply_markup=markup
    )

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id
    if chat_id not in load_users():
        return

    word = get_word_message()
    text = word if word else "❌ No more words left!"

    keyboard = [[InlineKeyboardButton("Generate Another", callback_data='generate')]]
    markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=markup
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))
    print("Bot running...")
    app.run_polling()

if __name__ == '__main__':
    main()
