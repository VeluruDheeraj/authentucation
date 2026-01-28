import sqlite3
from flask import g
DB="users.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db=g.pop("db",None)
    if db:
        db.close()

def init_db():
    db=sqlite3.connect(DB)
    cur=db.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password BLOB,
            role TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT ,
            author TEXT,
            available INTEGER
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS borrowed_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            book_id INTEGER,
            borrowed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (USER_ID) References users(id),
            FOREIGN KEY (BOOK_ID) REFERENCES books(id)
            
                
        )
    """)
    db.commit()
    db.close()

    