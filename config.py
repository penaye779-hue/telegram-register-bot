import os
from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")

DATABASE_URL = os.getenv("DATABASE_URL")

OTP_EXPIRY_MINUTES = int(
    os.getenv("OTP_EXPIRY_MINUTES", 5)
)



BOT_TOKEN = "8809207095:AAEIALdnd7EVuYyjS2Vdis-342IDKgAD6ck"