
import sqlite3

def create_tables(curs,conn):
  curs.execute('''CREATE TABLE IF NOT EXISTS games (
  id  INT,
  title TEXT,
  type TEXT,
  release_date TEXT,
  price TEXT)'''
  );
  curs.execute('''CREATE TABLE IF NOT EXISTS release_details (
  id  INTEGER PRIMARY KEY AUTOINCREMENT,
  game_id TEXT,
  platform TEXT)'''
  );
  curs.execute('''CREATE TABLE IF NOT EXISTS games_details (
  id  INTEGER PRIMARY KEY AUTOINCREMENT,
  game_id TEXT,
  publisher TEXT,
  description TEXT)'''
  );
  conn.commit()