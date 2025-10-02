import os
from telegram.ext import Application, CommandHandler

# /start command
async def start(update, context):
    await update.message.reply_text("👋 Hello! Your bot is running successfully.")

def main():
    TOKEN = os.getenv("BOT_TOKEN")  # Render မှာ BOT_TOKEN အနေနဲ့ ထည့်မယ်
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
