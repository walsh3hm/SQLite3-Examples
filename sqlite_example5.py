import sqlite3
conn = sqlite3.connect("my_sqlite.db")
cursor = conn.cursor()
#sql Select statement
sql = 'update hobbies set hobby = "coding and nano-electronics" where id=1'
cursor.execute(sql)
#commit the change
conn.commit()
conn.close()
