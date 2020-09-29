import sqlite3

conn = sqlite3.connect('db.sqlite3')
print ("Opened database successfully")

conn.execute('CREATE TABLE computers (id INTEGER PRIMARY KEY,brand TEXT)')
conn.close()