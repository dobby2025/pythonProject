'''
파일명: Ex24-3-sqlite-dml-update.py
'''

import sqlite3
conn = sqlite3.connect('hr.db')
cur = conn.cursor()

sql = "UPDATE employees SET first_name = ? WHERE employee_id = ?"

cur.execute(sql, ('PIKA', 1))
conn.commit()

cur.close()
conn.close()

