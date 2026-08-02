import sqlite3

def create_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        phone_number TEXT,
        otp TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_user(telegram_id, phone_number, otp):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users
    (telegram_id, phone_number, otp)
    VALUES (?, ?, ?)
    """,
    (
        telegram_id,
        phone_number,
        otp
    ))

    conn.commit()
    conn.close()


def get_user(telegram_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT phone_number, otp
    FROM users
    WHERE telegram_id = ?
    ORDER BY id DESC
    LIMIT 1
    """,
    (telegram_id,))

    result = cursor.fetchone()

    conn.close()

    return result