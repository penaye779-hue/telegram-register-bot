import os
from dotenv import load_dotenv

# Load local .env only if it exists (for local development)
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Retrieve DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Fix 1: Ensure it's not None or empty
if not DATABASE_URL:
  raise ValueError(
      "DATABASE_URL is not set! Check your Railway Environment Variables."
  )

# Fix 2: Railway postgres URLs start with postgres://, but psycopg2 requires postgresql://
if DATABASE_URL.startswith("postgres://"):
  DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

OTP_EXPIRY_MINUTES = int(os.getenv("OTP_EXPIRY_MINUTES", 5))

