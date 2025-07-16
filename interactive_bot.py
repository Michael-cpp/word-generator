from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from utils import pop_random_word, save_user

import os

BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    save_user(chat_id)
    
    keyboard = [[InlineKeyboardButton("Generate", callback_data='generate')]]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Welcome! Click 'Generate' to learn a new Russian word.",
        reply_markup=markup
    )

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    word = pop_random_word()
    if word:
        await query.edit_message_text(text=word)
    else:
        await query.edit_message_text(text="❌ No more words left!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))
    print("Bot running...")
    app.run_polling()

if __name__ == '__main__':
    main()
