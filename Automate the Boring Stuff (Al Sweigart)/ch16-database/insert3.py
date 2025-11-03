import sqlite3

conn = sqlite3.connect('ch16-database/database/example.db', isolation_level=None)
conn.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL, birthdate TEXT,\
fur TEXT, weight_kg REAL) STRICT')
update = conn.execute('INSERT INTO cats VALUES ("Zophie", "2021-01-24", "black", 5.6)')
