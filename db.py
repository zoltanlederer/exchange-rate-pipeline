import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    """Create and return a connection to the PostgreSQL database."""
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    dbname = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    return psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)

def setup_database():
    """Create exchange_rates table in database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            base_currency CHAR(3) NOT NULL,
            target_currency CHAR(3) NOT NULL,
            rate FLOAT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE (date, target_currency)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Database ready.")

setup_database()
