import sqlite3

conn = sqlite3.connect('room.db')
cursor = conn.cursor()


select_query = "SELECT * FROM room"
cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()