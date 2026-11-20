"""Database connection and schema setup (SQLite).

This module owns the connection and table definitions. Business rules live
in services.py, and the CLI lives in menu.py, so this file can be changed
without touching either of them.
"""

import sqlite3

DEFAULT_DB_PATH = "heritage.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS traditions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    community   TEXT NOT NULL,
    description TEXT NOT NULL,
    created_by  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS events (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name  TEXT NOT NULL,
    event_date  TEXT NOT NULL,
    location    TEXT NOT NULL,
    created_by  TEXT NOT NULL
);
"""


class Database:
    """Thin wrapper around a sqlite3 connection.

    All SQL in the application is passed as parameterized queries, which
    protects against SQL injection from user-typed text.
    """

    def __init__(self, path=DEFAULT_DB_PATH):
        self.path = path
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def execute(self, sql, params=()):
        """Run a write statement and commit it. Returns the cursor."""
        cursor = self.conn.execute(sql, params)
        self.conn.commit()
        return cursor

    def fetch_all(self, sql, params=()):
        """Run a read statement and return all rows."""
        return self.conn.execute(sql, params).fetchall()

    def fetch_one(self, sql, params=()):
        """Run a read statement and return one row, or None."""
        return self.conn.execute(sql, params).fetchone()

    def close(self):
        self.conn.close()
