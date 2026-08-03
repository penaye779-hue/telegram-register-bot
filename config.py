import os
from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")

DATABASE_URL = os.getenv("DATABASE_URL")

OTP_EXPIRY_MINUTES = int(
    os.getenv("OTP_EXPIRY_MINUTES", 5)
)



BOT_TOKEN = "8847569845:AAFrOoQxf9WxTmACDW2IPC7Zd-X_CX9_Rt8"