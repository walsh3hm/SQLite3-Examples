#import the built-in sqlite3 module
import sqlite3
#create or connect to an existing db
conn = sqlite3.connect("my_sqlite.db")
#get a cursor to work withthe db
#a db cursor is an object used to pinpoint records in a db
cursor = conn.cursor()
#close the connection to the db
conn.close()
