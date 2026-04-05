import sqlite3

#connect to db
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

#create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

#Insert data to table
cursor.execute('''INSERT INTO users(name, age) VALUES('Alice', 25)''')
conn.commit()

#Query data from table
cursor.execute('''SELECT * FROM users''')
print(cursor.fetchall())