import sqlite3
conn = sqlite3.connect("my_sqlite.db")
cursor = conn.cursor()
sql = "create table hobbies(id integer PRIMARY KEY, name text, sex text, age int, hobby text)"
cursor.execute(sql)
#commit the changes to the db
conn.commit()
conn.close()
