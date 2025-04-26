from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✅ Accept", callback_data="accept_policy")],
        [InlineKeyboardButton("❌ Decline", callback_data="decline_policy")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "EduBot Privacy Policy:\n\n"
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
        keyboard = [
            [InlineKeyboardButton("📘 MATHEMATICS-4", url="https://t.me/+xptlohHZTVJiMjRl")],
            [InlineKeyboardButton("📗 PYTHON", url="https://t.me/+Bs-3VsJ8SudjODY1")],
            [InlineKeyboardButton("📕 DATA STRUCTURE", url="https://t.me/+FO71qS8v7RNmMWNl")],
            [InlineKeyboardButton("🎬 MOVIES", url="https://t.me/techmovie2025")],
            [InlineKeyboardButton("🧑‍💻 CHAT-GROUP", url="https://t.me/Btech_course")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Welcome to EduBot!\n\nJoin a study group and get started:",
            reply_markup=reply_markup
        )
    else:
        await query.edit_message_text("You must accept the Privacy Policy to use this bot.")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/notes - Get subject notes\n"
        "/quiz - Take a quiz\n"
        "/video - Watch a video\n"
        "/contact - Contact info\n"
        "/privacy - Privacy & Data Policy"
    )

# /notes command
async def notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Choose a subject:\n"
        "📘 Maths Notes: https://example.com/maths_notes\n"
        "📗 Physics Notes: https://example.com/physics_notes"
    )

# /video command
async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Watch this lecture on AI Basics:\nhttps://youtube.com/example"
    )

# /contact command
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Email: support@edubot.in\nTelegram: @yourusername")

# /privacy command
async def privacy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "EduBot Privacy Policy:\n\n"
        "We respect your privacy. This bot does not collect, store, or share any personal information.\n"
        "By using this bot, you agree to our Privacy Terms in compliance with GDPR & IT Act 2000."
    )

# Build the bot app
app = ApplicationBuilder().token("7992343355:AAF81Y88btBBv4fFLyj_ILauuaSeQA4p1Co").build()

# Register Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_policy_response))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("notes", notes))
app.add_handler(CommandHandler("video", video))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("privacy", privacy))

# Run the bot
app.run_polling()