import sqlite3

conn = sqlite3.connect('ch16-database/database/example.db', isolation_level=None)
result = conn.execute('SELECT * FROM cats').fetchall()
print(result)