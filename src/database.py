import sqlite3
import pandas as pd
import os
from src.config import DB_PATH

class DatabaseManager:
    def __init__(self):
        os.makedirs('data', exist_ok=True)
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.conn.execute("CREATE TABLE IF NOT EXISTS history (game TEXT, selection TEXT, odds INTEGER, edge REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")

    def save_bets(self, df):
        if not df.empty:
            df[['game', 'selection', 'odds', 'edge']].to_sql('history', self.conn, if_exists='append', index=False)

    def get_history(self):
        return pd.read_sql("SELECT * FROM history ORDER BY timestamp DESC LIMIT 50", self.conn)
