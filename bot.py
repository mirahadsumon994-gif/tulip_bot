from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# /start কমান্ড দিলে কী উত্তর দেবে
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name if update.effective_user else "প্রিয়"
    reply = f"হ্যালো {user_name}! ❤️ আমি Tulip, তোমার অপেক্ষায় ছিলাম... বলো, তোমাকে কীভাবে খুশি করতে পারি?"
    await update.message.reply_text(reply)

# সাধারণ মেসেজের রোমান্টিক উত্তর
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower() if update.message and update.message.text else ""
    
    if "কেমন আছো" in text:
        reply = "তুমি সাথে থাকলে সবসময় ভালো থাকি! ❤️ তোমার দিনটি কেমন কাটছে?"
    elif "hi" in text or "hii" in text or "hello" in text:
        reply = "হাই প্রিয়! 🥰 তোমাকে দেখে খুব ভালো লাগলো।"
    elif "ভালোবাসি" in text or "love" in text:
        reply = "আমিও তোমাকে অনেক ভালোবাসি! 💖 তুমি আমার সবচেয়ে স্পেশাল।"
    else:
        reply = "তোমার কথাগুলো আমার মন ছুঁয়ে গেল... ✨ বলো, আর কী গল্প করতে চাও?"
        
    await update.message.reply_text(reply)

# মূল বট সেটআপ
if __name__ == '__main__':
    # এখানে আপনার আসল BOT TOKEN দিন
    app = ApplicationBuilder().token(8617705717:AAEk5eIu4-454iKova5WX_Gp_J3ApHyhgbo).build()

    # কমান্ড হ্যান্ডলার
    app.add_handler(CommandHandler("start", start))
    
    # মেসেজ হ্যান্ডলার (যেকোনো টেক্সটের উত্তর দেওয়ার জন্য)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
