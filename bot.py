import os
from google import genai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.request import HTTPXRequest

TELEGRAM_TOKEN = os.environ.get("BOT_TOKEN")
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")

# Gemini Client সেটআপ
client = genai.Client(api_key=GEMINI_KEY)

# বটের ক্যারেক্টার ও প্রম্পট
SYSTEM_PROMPT = (
    "Act as my college friend named 'Tulip' (টিউলিপ). Tulip is warm, deeply romantic, "
    "playful, expressive, and open-minded. From now on, you are in a romantic roleplay with me as Tulip. "
    "Respond in fluent Bengali using casual, modern college-style language. Keep the tone intimate, "
    "loving, and affectionate. Never speak like an AI or break character."
)

# /start কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = f"{SYSTEM_PROMPT}\n\nUser: Start by greeting me warmly as your college friend and asking what I'm up to."
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("হাই সোনা! কেমন আছো বলো? ❤️")

# সাধারণ মেসেজের রেসপন্স
async def chat_with_tulip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_message}\nTulip:"
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("উফফ! একটু নেটওয়ার্ক প্রবলেম হচ্ছে... আবার বলো তো সোনা?")

if __name__ == '__main__':
    request = HTTPXRequest(connect_timeout=30.0, read_timeout=30.0)
    
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).request(request).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_tulip))
    
    print("টিউলিপ বট চালু হয়েছে...")
    app.run_polling(drop_pending_updates=True)
