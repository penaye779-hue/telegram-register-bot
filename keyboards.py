# ===========================
# Tinder Connect Premium Keyboards
# ===========================

from telegram import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


# ===========================
# PHONE REQUEST BUTTON
# ===========================

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
        input_field_placeholder="Tap to continue..."
    )


# ===========================
# MAIN DASHBOARD
# ===========================

def main_menu():

    buttons = [

        [
            InlineKeyboardButton(
                "🚀 Get Started",
                callback_data="start_registration"
            )
        ],


        [
            InlineKeyboardButton(
                "❓ Help",
                callback_data="help"
            )
        ],

        [
            InlineKeyboardButton(
                "🌐 Website",
                url="https://tinder.com/"
            )
        ]

    ]

    return InlineKeyboardMarkup(buttons)



# ===========================
# HELP MENU
# ===========================

def help_menu():

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "💬 Contact Support",
                    url="https://t.me/@dategram_support_bot"
                )
            ],
            [
                InlineKeyboardButton(
                    "⬅️ Back",
                    callback_data="main_menu"
                )
            ]
        ]
    )



# ===========================
# AFTER REGISTRATION MENU
# ===========================

def dashboard_menu():

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "👤 My Profile",
                    callback_data="profile"
                )
            ],

            [
                InlineKeyboardButton(
                    "⚙️ Settings",
                    callback_data="settings"
                )
            ],

            [
                InlineKeyboardButton(
                    "💎 Premium",
                    callback_data="premium"
                )
            ]
        ]
    )