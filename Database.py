import sqlite3

# สร้างการเชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect('mydatabase.db')

# สร้าง cursor object
cursor = conn.cursor()

# สร้างตารางถ้ายังไม่มีอยู่
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# เพิ่มข้อมูลถ้าไม่มีข้อมูล
cursor.execute('''
INSERT INTO users (name, email)
VALUES ('John Doe', 'john@example.com')
''')

# อ่านข้อมูลจากตาราง users
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
print("Users in the database:")
for user in users:
    print(user)

# อัปเดตข้อมูล
cursor.execute('''
UPDATE users
SET name = 'Icesu Doe'
WHERE id = 1
''')

# ลบข้อมูล
cursor.execute('''
DELETE FROM users
WHERE id = 1
''')

# ดูรายชื่อตารางทั้งหมดในฐานข้อมูล
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])

# ปิดการเชื่อมต่อ
conn.commit()
conn.close()
