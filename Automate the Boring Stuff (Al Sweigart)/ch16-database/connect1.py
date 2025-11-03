import sqlite3

conn = sqlite3.connect('ch16-database/database/example.db', isolation_level=None)

conn.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL,\
birthdate TEXT, fur TEXT, weight_kg REAL) STRICT')

# There are six data types in SQLite:

# NULL Analogous to Python’s None

# INT or INTEGER Analogous to Python’s int type

# REAL A reference to the mathematics term real number; analogous to Python’s float type

# TEXT Analogous to Python’s str type

# BLOB Short for Binary Large Object; analogous to Python’s bytes type and useful for storing entire files in a database

