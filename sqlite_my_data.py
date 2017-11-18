import sqlite3
conn = sqlite3.connect("my_sqlite.db")
cursor = conn.cursor()
sql = "insert into hobbies values (?,?,?,?,?)"
data = (4, "Hannah", "Female", 21, "shopping")
cursor.execute(sql, data)
conn.commit()
conn.close()
