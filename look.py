import sqlite3

# สร้างการเชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect('mydatabase.db')

# สร้าง cursor object
cursor = conn.cursor()

# ใช้คำสั่ง SQL เพื่อดูข้อมูลทั้งหมดในตาราง users
cursor.execute('SELECT * FROM users')

# ดึงข้อมูลทั้งหมดและพิมพ์ผลลัพธ์
users = cursor.fetchall()
print("Users in the database:")
for user in users:
    print(user)

# ปิดการเชื่อมต่อ
conn.close()