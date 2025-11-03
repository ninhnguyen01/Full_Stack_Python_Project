import sqlite3

conn = sqlite3.connect('ch16-database/database/example.db', isolation_level=None)
conn.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL, birthdate TEXT,\
fur TEXT, weight_kg REAL) STRICT')

cat_name = 'Zophie'
cat_bday = '2021-01-24'
fur_color = 'black'
cat_weight = 5.6

conn.execute('INSERT INTO cats VALUES (?, ?, ?, ?)', [cat_name, cat_bday,
fur_color, cat_weight])
