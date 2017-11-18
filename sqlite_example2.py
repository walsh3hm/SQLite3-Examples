import sqlite3
conn = sqlite3.connect("my_sqlite.db")
cursor = conn.cursor()
#data supplied as tuple. ? - are place holders for data
sql = "insert into hobbies values (?,?,?,?,?)"
data = (1, "Tony", "male", 23, "coding")
cursor.execute(sql, data)
#commit the changes to db
conn.commit()
conn.close()
