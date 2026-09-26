import os 
from dotenv import load_dotenv
load_dotenv()

SQLITE_DATABASE=os.getenv("SQLITE_DATABASE", "agent_logs.db")
SQLITE_TABLE_NAME=os.getenv("SQLITE_TABLE_NAME",'agent_logs')

import sqlite3

def create_database():
    # Connect to SQLite database (creates 'agent_logs.db' if it doesn't exist)
    conn = sqlite3.connect(SQLITE_DATABASE)
    cursor = conn.cursor()

    # Create the agent_and_tool_call_logs table
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {SQLITE_TABLE_NAME} (
            chat_id TEXT ,
            session_id TEXT ,
            user_id TEXT ,
            agent_name TEXT,
            tool_name TEXT,
            tool_arguments TEXT);""")

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database and table created successfully.")