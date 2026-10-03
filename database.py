import sqlite3

DATABASE_PATH = "data/placement.db"


def get_connection():
    """Create and return a connection to the SQLite database."""
    return sqlite3.connect(f"file:{DATABASE_PATH}?mode=ro", uri=True)

    