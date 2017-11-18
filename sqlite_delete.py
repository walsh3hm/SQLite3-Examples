import sqlite3
conn = sqlite3.connect("my_sqlite.db")
cursor = conn.cursor()
DELETE ("my_sqlite.db")
WHERE id = 5
cursor.execute(sql. data)
conn.commit()
conn.close()

