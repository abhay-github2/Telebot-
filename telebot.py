from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = "7992343355:AAF81Y88btBBv4fFLyj_ILauuaSeQA4p1Co"
bot = Bot(token=TOKEN)
app = Flask(__name__)
dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✅ Accept", callback_data="accept_policy")],
        [InlineKeyboardButton("❌ Decline", callback_data="decline_policy")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "BOT Privacy Policy:\n\n"
        "We respect your privacy. This bot does not collect, store, or share any personal information.\n"
        "By using this bot, you agree to our Privacy Terms.\n\n"
        "Do you accept?",
        reply_markup=reply_markup
    )

# Handle acceptance or decline
async def handle_policy_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "accept_policy":
        context.user_data["accepted_policy"] = True 
        user_first_name = update.effective_user.first_name
        welcome_text = f"Hello {user_first_name}!"
        keyboard = [
            [InlineKeyboardButton("📘 MATHEMATICS-4", url="https://t.me/+-x-5jIjLbSsyMjc1")],
            [InlineKeyboardButton("📒🔖 ONE SHORT LECTURE", url="https://t.me/+0gwqmIQXTbQxNWM1")],
            [InlineKeyboardButton("📗 PYTHON", url="https://t.me/+fqycovjNK-U3OTM1")],
            [InlineKeyboardButton("📕 DATA STRUCTURE", url="https://t.me/+OgloXv7bzsQ3MTBl")],
            [InlineKeyboardButton("📔 CO & CA", url="https://t.me/+Qhw7v4kWSvwwOTE1")],
            [InlineKeyboardButton("📘 DSTL", url="https://t.me/+N8GsUFP6XshmMTNl")],
            [InlineKeyboardButton("📕 TECHNICAL COMMUNEMITION ", url="https://t.me/+nWQpJCdh_7k5YThl")],
            [InlineKeyboardButton("📔 EMFT", url="https://t.me/+lN5VlRtFMr9iZTFl")],
            [InlineKeyboardButton("📗 EMI", url="https://t.me/+6GZX8mQiNRlmNzk1")],
            [InlineKeyboardButton("📙 BSS", url="https://t.me/+_zXVLEjdE0FhN2Nl")],
            [InlineKeyboardButton("📘 DSD & DE", url="https://t.me/+tabUbigyyQxiZGY1")],
            [InlineKeyboardButton("👨‍💻 CHAT GROUP", url="https://t.me/Btech_course")],
            [InlineKeyboardButton("🎬 MOVIE", url="https://t.me/techmovie2025")],
            [InlineKeyboardButton("📗 NOTES", url="https://t.me/+yxayMFNw16IzOWI9")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            welcome_text + "\n\nJoin a study group and get started:",
            reply_markup=reply_markup
        )
    else:
        await query.edit_message_text("You must accept the Privacy Policy to use this bot.")

# Other commands
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/notes - Get subject notes\n"
        "/quiz - Take a quiz\n"
        "/video - Watch a video\n"
        "/contact - Contact info\n"
        "/privacy - Privacy & Data Policy"
    )

async def notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Choose a subject:\n"
        "📘 Maths Notes: https://example.com/maths_notes\n"
        "📗 Physics Notes: https://example.com/physics_notes"
    )

async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Watch this lecture on AI Basics:\nhttps://youtube.com/example"
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Email: support@edubot.in\nTelegram: @yourusername")

async def privacy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "BTECHAIMLBOT Privacy Policy:\n\n"
        "We respect your privacy. This bot does not collect, store, or share any personal information.\n"
        "By using this bot, you agree to our Privacy Terms in compliance with GDPR & IT Act 2000."
    )

# Register Handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(handle_policy_response))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(CommandHandler("notes", notes))
dispatcher.add_handler(CommandHandler("video", video))
dispatcher.add_handler(CommandHandler("contact", contact))
dispatcher.add_handler(CommandHandler("privacy", privacy))

# Flask Webhook Routes
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running with Flask!"

# For local run (optional)
if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 10000)))
