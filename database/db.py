"""SQLite data layer for Spendly.

get_db()  — connection with dict-like rows and foreign key enforcement
init_db() — creates all tables using CREATE TABLE IF NOT EXISTS
seed_db() — inserts demo user and sample expenses for development
"""

import os
import sqlite3
from datetime import date

from werkzeug.security import generate_password_hash

# expense_tracker.db lives in the project root, one level up from database/.
# Derived from __file__ rather than the cwd so the path is stable no matter
# where `python app.py` is invoked from.
DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "expense_tracker.db",
)

# Fixed category list — reused by expense forms and validation in later steps.
CATEGORIES = ["Food", "Transport", "Bills", "Health",
              "Entertainment", "Shopping", "Other"]


# ------------------------------------------------------------------ #
# Connection                                                          #
# ------------------------------------------------------------------ #

def get_db():
    """Return a connection with row_factory and foreign keys enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    # foreign_keys is a per-connection pragma, so it must be set on every open.
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# ------------------------------------------------------------------ #
# Schema                                                              #
# ------------------------------------------------------------------ #

def init_db():
    """Create both tables. Safe to call repeatedly."""
    conn = get_db()
    try:
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id            INTEGER PRIMARY KEY AUTOINCREMENT,
                    name          TEXT NOT NULL,
                    email         TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL,
                    created_at    TEXT NOT NULL DEFAULT (datetime('now'))
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id     INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                    amount      REAL    NOT NULL,
                    category    TEXT    NOT NULL,
                    date        TEXT    NOT NULL,
                    description TEXT,
                    created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
                )
            """)
    finally:
        conn.close()


# ------------------------------------------------------------------ #
# Sample data                                                         #
# ------------------------------------------------------------------ #

def seed_db():
    """Insert the demo user and 8 sample expenses, once."""
    conn = get_db()
    try:
        if conn.execute("SELECT 1 FROM users LIMIT 1").fetchone():
            return

        today = date.today()

        def day(n):
            """Date in the current month, YYYY-MM-DD."""
            return "{:04d}-{:02d}-{:02d}".format(today.year, today.month, n)

        with conn:
            cur = conn.execute(
                "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
                ("Demo User", "demo@spendly.com", generate_password_hash("demo123")),
            )
            user_id = cur.lastrowid

            # One expense per category, plus a second Food row — 8 total.
            # Days 2-21 exist in every month.
            conn.executemany(
                "INSERT INTO expenses (user_id, amount, category, date, description) "
                "VALUES (?, ?, ?, ?, ?)",
                [
                    (user_id, 450.00, "Food", day(2), "Groceries for the week"),
                    (user_id, 120.50, "Transport", day(4), "Metro card top-up"),
                    (user_id, 1899.00, "Bills", day(6), "Electricity bill"),
                    (user_id, 650.00, "Health", day(9), "Pharmacy — monthly medication"),
                    (user_id, 299.00, "Entertainment", day(12), "Streaming subscription"),
                    (user_id, 2450.75, "Shopping", day(15), "Running shoes"),
                    (user_id, 180.00, "Other", day(18), "Notebook and stationery"),
                    (user_id, 320.00, "Food", day(21), "Dinner with friends"),
                ],
            )
    finally:
        conn.close()
