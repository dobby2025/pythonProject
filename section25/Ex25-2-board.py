'''
파일명: Ex25-2-board.py
'''

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as msg
import sqlite3

class BoardApp(tk.Tk):
    def __init__(self):     # BoardApp 생성자
        super().__init__()

        self.title('게시판')

        self.combobox_search = ttk.Combobox(self)  # 검색 콤보 박스
        self.textfield_search = tk.Entry(self)  # 검색 텍스트 필드
        self.button_search = tk.Button(self, text='검색', command=self.onclick_search)  # 검색 버튼
        self.button_insert = tk.Button(self, text='신규')  # 신규 버튼
        self.button_update = tk.Button(self, text='수정')  # 수정 버튼
        self.button_delete = tk.Button(self, text='삭제')  # 삭제 버튼
        self.treeview_boardList = ttk.Treeview(self,
                                               columns=('id', 'title', 'writer', 'date'),
                                               show='headings'
                                               )  # 가운데 트리뷰

        # 컨트롤 배치
        self.combobox_search.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.textfield_search.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        self.button_search.grid(row=0, column=2, padx=5, pady=5, sticky='ns')
        self.treeview_boardList.grid(row=1, column=0, rowspan=3, columnspan=2,
                                     padx=5, pady=5, sticky='nsew')
        self.button_insert.grid(row=1, column=2, padx=5, pady=5, sticky='ns')
        self.button_update.grid(row=2, column=2, padx=5, pady=5, sticky='ns')
        self.button_delete.grid(row=3, column=2, padx=5, pady=5, sticky='ns')

        # 트리뷰 컬럼 설정
        self.treeview_boardList.heading('id', text='ID')
        self.treeview_boardList.column('id', width=50)
        self.treeview_boardList.heading('title', text='제목')
        self.treeview_boardList.column('title', width=300)
        self.treeview_boardList.heading('writer', text='작성자')
        self.treeview_boardList.column('writer', width=100)
        self.treeview_boardList.heading('date', text='작성일')
        self.treeview_boardList.column('date', width=150)

        # 검색 기준 설정
        self.combobox_search['values'] = ('제목', '작성자')
        self.combobox_search.current(0)
        
        # 초기화면 데이터 검색
        self.initBoardList()

    # 게시판 초기화
    def initBoardList(self):

        rows = self.getBoardList()

        # 트리뷰 초기화
        self.treeview_boardList.delete(*self.treeview_boardList.get_children())
        self.treeview_boardList.bind('<Double-Button-1>', self.onclick_view)

        for row in rows:
            self.treeview_boardList.insert('', 'end', text='',
                                       values=row)

    def getBoardList(self, keyword='', select_option=''):
        conn = sqlite3.connect('py_board.db')
        curs = conn.cursor()
        
        # 검색 조건에 따른 WHERE 절 구성
        if select_option == '작성자' and keyword != '':
            where_clause = "WHERE BOARD_WRITER = :1"
        else:
            where_clause = "WHERE BOARD_TITLE LIKE '%' || :1 || '%'"

        sql =f'''
        SELECT BOARD_ID, BOARD_TITLE, BOARD_WRITER, BOARD_DATE
        FROM PY_BOARD
        {where_clause}
        ORDER BY BOARD_ID DESC
        '''
        curs.execute(sql,(keyword,))
        rows = curs.fetchall()

        curs.close()
        conn.close()

        return rows

    # 검색버튼 클릭
    def onclick_search(self):

        keyword = self.textfield_search.get()

        search_option = self.combobox_search.get()

        # PY_BOARD 데이터 불러오기
        rows = self.getBoardList(keyword, search_option)

        # 트리뷰 초기화
        self.treeview_boardList.delete(*self.treeview_boardList.get_children())
        self.treeview_boardList.bind('<Double-Button-1>', self.onclick_view)

        # 게시글 목록 출력
        for row in rows:
            self.treeview_boardList.insert('', 'end', text='', values=row)


    def onclick_view(self, event):
        selection = self.treeview_boardList.selection()

        if not selection:
            return

        board_id = self.treeview_boardList.item(selection, 'values')[0]

        row = self.get_board(board_id)  # 게시글 상세조회
        view_dialog = BoardViewDialog(self, row)
        self.wait_window(view_dialog)


    def get_board(self, board_id):
        conn = sqlite3.connect('py_board.db')
        curs = conn.cursor()

        sql = f'''
                SELECT BOARD_ID, BOARD_TITLE, BOARD_WRITER, BOARD_CONTENT, BOARD_DATE
                FROM PY_BOARD
                WHERE BOARD_ID = :1                
                '''
        curs.execute(sql, (board_id,))
        row = curs.fetchone()

        curs.close()
        conn.close()

        return row


class BoardViewDialog(tk.Toplevel):

    def __init__(self, parent, row):
        super().__init__(parent)
        self.title('게시글 보기')

        # 컨트롤 변수 선언
        self.label_title = tk.Label(self, text=row[1], font=('Arial', 14, 'bold'))
        self.label_writer = tk.Label(self, text=row[2], font=('Arial', 12))
        self.textarea_content = scrolledtext.ScrolledText(self)
        self.button_close = tk.Button(self, text='닫기', command=self.destroy)

        # 컨트롤 배치
        self.label_title.pack(side=tk.TOP, padx=5, pady=5)
        self.label_writer.pack(side=tk.TOP, padx=5, pady=5)
        self.textarea_content.pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH, expand=True)
        self.button_close.pack(side=tk.RIGHT, padx=5, pady=5)

        # 게시글 내용 출력
        self.textarea_content.insert(tk.END, row[3])

        self.geometry('+%d+%d' % (parent.winfo_rootx() + parent.winfo_width() / 2 - self.winfo_width() / 2,
                                  parent.winfo_rooty() + parent.winfo_height() / 2 - self.winfo_height() / 2
                                  ))
















# 실행코드
if __name__ == '__main__':
    app = BoardApp()
    app.mainloop()






        
        







