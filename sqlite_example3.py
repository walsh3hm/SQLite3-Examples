import sqlite3
conn = sqlite3.connect("my_sqlite.db")
cursor = conn.cursor()
#data supplied as a tuple of tuples. / - placeholders for data
sql = "insert into hobbies values (?,?,?,?,?)"
data = ( (2, "Sarah", "female", 22, "guitar"), (3, "Jean", "female", 21, "bowling") )
cursor.executemany(sql, data)
#commit the changes
conn.commit()
conn.close()
