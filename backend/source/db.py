import psycopg2
import psycopg2.extras

from source.config import DATABASE_URL


def get_db():
    conn = psycopg2.connect(DATABASE_URL)
    # Возвращаем словари вместо кортежей
    conn.cursor_factory = psycopg2.extras.RealDictCursor 
    return conn

def init_db():
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS snippets (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
        conn.commit()
