import sqlite3
import Flask
sql = ""
conn = sqlite3.connect("sqlite.db")
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
conn.close()

