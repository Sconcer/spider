import sqlite3
sql = ""
conn = sqlite3.connect("sqlite.db")
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
conn.close()
