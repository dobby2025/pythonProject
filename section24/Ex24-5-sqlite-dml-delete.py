'''
파일명: Ex24-5-sqlite-dml-delete.py
'''
import sqlite3
conn = sqlite3.connect('hr.db')
cur = conn.cursor()

sql = "DELETE FROM employees WHERE employee_id = ?"

cur.execute(sql, ('2'))
conn.commit()

cur.close()
conn.close()