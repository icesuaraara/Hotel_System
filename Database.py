import sqlite3

# สร้างการเชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect('room.db')

# สร้างเคอร์เซอร์เพื่อทำการดำเนินการกับฐานข้อมูล
cursor = conn.cursor()

# คำสั่ง SQL สำหรับสร้างตาราง room
create_table_query = '''
CREATE TABLE IF NOT EXISTS room (
    room_info TEXT,
    room_id INTEGER PRIMARY KEY,
    id_customer INTEGER,
    customer_count INTEGER,
    bed INTEGER,
    status_room TEXT,
    use_status_day INTEGER
)
'''

cursor.execute(create_table_query)

# ปิดการเชื่อมต่อกับฐานข้อมูล
conn.commit()
conn.close()

print("Database and table created successfully.")