from telegram import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def phone_keyboard():
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(
                    text="📱 Share Phone Number",
                    request_contact=True
                )
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Tap the button to continue..."
    )


def main_menu():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🌐 Website",
                    url="https://yourwebsite.com"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔒 Privacy Policy",
                    url="https://yourwebsite.com/privacy"
                )
            ],
            [
                InlineKeyboardButton(
                    "❓ Support",
                    url="https://t.me/YourSupport"
                )
            ]
        ]
    )