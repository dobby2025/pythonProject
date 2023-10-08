'''
파일명: Ex24-4-sqlite-dml-select.py
'''

import sqlite3
conn = sqlite3.connect('hr.db')
cur = conn.cursor()

sql = "SELECT * FROM employees "
cur.execute(sql)
rows = cur.fetchall()
print(rows)

