import pytest
import datetime
import sqlite3

@pytest.fixture
def curtime():
    # Get the current date and time in UTC
    return datetime.datetime.now(datetime.UTC)

@pytest.fixture
def dbconn():
    # Initialize a memory-based SQLite database connection
    return sqlite3.connect(":memory:")

def test_something(curtime, dbconn):
    print("In test_something()")
    print("Current time is", curtime)
    print("The database connection is", dbconn)

def test_another(curtime, dbconn):
    print("In test_another()")
    print("Current time is", curtime)
    print("The database connection is", dbconn)
    