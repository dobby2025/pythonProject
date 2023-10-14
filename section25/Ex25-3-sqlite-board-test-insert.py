import sqlite3

conn = sqlite3.connect('py_board.db')
curs = conn.cursor()

# 데이터 삽입
sql = '''
INSERT INTO PY_BOARD(BOARD_TITLE, BOARD_WRITER, BOARD_CONTENT)
VALUES(?, ?, ?)
'''
curs.execute(sql, ('test', 'dev', '테스트중입니다.'))
conn.commit()
curs.close()
conn.close()

conn = sqlite3.connect('py_board.db')
curs = conn.cursor()

sql = "SELECT * FROM PY_BOARD "
curs.execute(sql)
rows = curs.fetchall()
print(rows)

curs.close()
conn.close()
