import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

SQLITE_DATABASE = os.getenv("SQLITE_DATABASE", "agent_logs.db")


def execute_query(query, params=()):
    """Executes any write query (INSERT, UPDATE, DELETE, CREATE)."""
    conn = sqlite3.connect(SQLITE_DATABASE)
    cursor = conn.cursor()

    cursor.execute(query, params)

    conn.commit()
    conn.close()


def fetch_query(query, params=()):
    """Executes any SELECT query and returns all matching rows."""
    conn = sqlite3.connect(SQLITE_DATABASE)
    cursor = conn.cursor()

    cursor.execute(query, params)
    rows = cursor.fetchall()

    conn.close()
    return rows