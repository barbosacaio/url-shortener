import sqlite3

conn = sqlite3.connect('app/database/urls.db')

with open('app/database/schema.sql') as f:
    conn.executescript(f.read())

conn.close()