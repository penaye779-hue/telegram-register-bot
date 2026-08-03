import psycopg2
from config import DATABASE_URL


def connection():
    return psycopg2.connect(
        DATABASE_URL
    )


def create_tables():

    conn = connection()
    cur = conn.cursor()


    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id SERIAL PRIMARY KEY,

        telegram_id BIGINT UNIQUE NOT NULL,

        phone_number VARCHAR(20) NOT NULL,

        otp_hash TEXT,

        otp_verified BOOLEAN DEFAULT FALSE,

        otp_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


    conn.commit()

    cur.close()
    conn.close()



def create_user(
        telegram_id,
        phone_number,
        otp_hash
):

    conn = connection()
    cur = conn.cursor()


    cur.execute("""
    INSERT INTO users
    (
        telegram_id,
        phone_number,
        otp_hash
    )

    VALUES
    (%s,%s,%s)

    ON CONFLICT (telegram_id)

    DO UPDATE SET

    phone_number = EXCLUDED.phone_number,

    otp_hash = EXCLUDED.otp_hash,

    otp_verified = FALSE,

    otp_created_at = CURRENT_TIMESTAMP

    """,
    (
        telegram_id,
        phone_number,
        otp_hash
    ))


    conn.commit()

    cur.close()
    conn.close()



def get_user(telegram_id):

    conn = connection()
    cur = conn.cursor()


    cur.execute("""
    SELECT
    phone_number,
    otp_hash,
    otp_verified

    FROM users

    WHERE telegram_id=%s

    """,
    (telegram_id,))


    data = cur.fetchone()


    cur.close()
    conn.close()


    return data



def verify_user(telegram_id):

    conn = connection()
    cur = conn.cursor()


    cur.execute("""
    UPDATE users

    SET otp_verified=TRUE

    WHERE telegram_id=%s

    """,
    (telegram_id,))


    conn.commit()

    cur.close()
    conn.close()