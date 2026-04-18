import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "spendly.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    with get_db() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                name          TEXT    NOT NULL,
                email         TEXT    NOT NULL UNIQUE,
                password_hash TEXT    NOT NULL,
                created_at    TEXT    NOT NULL DEFAULT (date('now'))
            );

            CREATE TABLE IF NOT EXISTS expenses (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL REFERENCES users(id),
                amount      REAL    NOT NULL,
                category    TEXT    NOT NULL,
                description TEXT,
                date        TEXT    NOT NULL,
                created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
            );
        """)


def seed_db():
    with get_db() as conn:
        if conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] > 0:
            return

        conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            ("Nitish Kumar", "nitish@example.com", "pbkdf2:sha256:600000$placeholder$hash"),
        )
        user_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

        conn.executemany(
            "INSERT INTO expenses (user_id, amount, category, description, date) VALUES (?,?,?,?,?)",
            [
                (user_id, 4500.00, "Bills",     "Electricity + internet", "2026-03-05"),
                (user_id, 3200.00, "Food",      "Groceries and dining",   "2026-03-10"),
                (user_id, 2050.00, "Health",    "Gym membership",         "2026-03-12"),
                (user_id, 1800.00, "Transport", "Metro monthly pass",     "2026-03-01"),
                (user_id,  950.00, "Food",      "Weekend outing",         "2026-03-18"),
                (user_id,  600.00, "Bills",     "Mobile recharge",        "2026-03-20"),
            ],
        )
