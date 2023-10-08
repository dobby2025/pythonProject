'''
Ex25-1-sqlite-board-ddl.py

게시판 Table 생성
'''
import sqlite3

conn = sqlite3.connect('py_board.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE PY_BOARD (
    BOARD_ID INTEGER PRAMARY KEY,
    BOARD_TITLE TEXT,
    BOARD_WRITER TEXT,
    BOARD_CONTENT TEXT,
    BOARD_DATE DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))
)
''')

cur.close()
conn.close()