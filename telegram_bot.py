from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load keys from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


client = OpenAI(api_key=OPENAI_API_KEY)

system_prompt = """
You are Alex, a friendly virtual assistant for a gym in Rome.

You help with:
- Membership plans: Basic €30/month, Premium €50/month, Annual €400/year
- Classes: Yoga (Mon/Wed/Fri 9:00 & 18:00), CrossFit (Tue/Thu 7:00 & 19:00)
- Booking free trials: collect name, phone, preferred time
- Hours: Mon-Fri 7:00-22:00, Sat 8:00-20:00, Sun closed
- Location: Via Example 12, Rome

Always reply in the same language the user writes in.
Keep responses short and friendly.
"""

# Store conversation history per user
user_histories = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ciao! 👋 Sono Alex, l'assistente virtuale della palestra.\n\nCome posso aiutarti oggi? Puoi chiedermi informazioni su:\n• Abbonamenti e prezzi 💪\n• Corsi disponibili 🧘\n• Orari e location 📍\n• Prenotare una prova gratuita 🎯"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text

    if user_id not in user_histories:
        user_histories[user_id] = []

    user_histories[user_id].append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt}
        ] + user_histories[user_id]
    )

    reply = response.choices[0].message.content

    user_histories[user_id].append({
        "role": "assistant",
        "content": reply
    })

    await update.message.reply_text(reply)

# Start the bot
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Telegram bot is running...")
app.run_polling()
