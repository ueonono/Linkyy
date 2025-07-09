import aiosqlite
import os

DB_PATH = os.path.join("data", "marvelink.db")

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS profiles (
            user_id INTEGER PRIMARY KEY,
            marvel_id TEXT,
            pseudo TEXT,
            level INTEGER,
            rank TEXT,
            rank_icon TEXT,
            rank_color TEXT,
            total_matches INTEGER,
            total_wins INTEGER,
            winrate REAL,
            last_update DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)
        await db.execute("""
        CREATE TABLE IF NOT EXISTS hero_stats (
            user_id INTEGER,
            hero_id INTEGER,
            hero_name TEXT,
            hero_class TEXT,
            matches INTEGER,
            wins INTEGER,
            win_rate REAL,
            kills INTEGER,
            deaths INTEGER,
            assists INTEGER,
            play_time REAL,
            mode TEXT,
            PRIMARY KEY (user_id, hero_id, mode)
        );
        """)
        await db.execute("""
        CREATE TABLE IF NOT EXISTS match_history (
            user_id INTEGER,
            match_uid TEXT,
            hero_id INTEGER,
            hero_name TEXT,
            kills INTEGER,
            deaths INTEGER,
            assists INTEGER,
            is_win INTEGER,
            duration REAL,
            match_time_stamp INTEGER,
            PRIMARY KEY (user_id, match_uid)
        );
        """)
        await db.execute("""
        CREATE TABLE IF NOT EXISTS teammates (
            user_id INTEGER,
            teammate_uid INTEGER,
            teammate_name TEXT,
            matches INTEGER,
            wins INTEGER,
            win_rate REAL,
            PRIMARY KEY (user_id, teammate_uid)
        );
        """)
        await db.execute("""
        CREATE TABLE IF NOT EXISTS rank_history (
            user_id INTEGER,
            match_time_stamp INTEGER,
            level_from INTEGER,
            level_to INTEGER,
            add_score REAL,
            total_score REAL,
            PRIMARY KEY (user_id, match_time_stamp)
        );
        """)
        await db.commit()
