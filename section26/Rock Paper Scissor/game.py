'''
파일명: game.py
'''

import random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.grid()

        self.username = tk.StringVar()
        self.main_frame()

        self.userPoint = 0
        self.sysPoint = 0

    def main_frame(self):
        self.main = tk.Frame(self, width=400, height=300, bg='white')
        self.main.grid(row=0, column=0)
        self.main.grid_propagate(False)

        self.game_lbl = tk.Label(self.main, image=rps_icon)
        self.game_lbl.grid(row=0, column=0, columnspan=3, padx=90, pady=10)

        self.name_lbl = tk.Label(self.main, text='Enter your name : ',
                                 font='verdana 10', bg='white')
        self.name_lbl.grid(row=1, column=0, pady=10)

        self.name_entry = ttk.Entry(self.main, textvariable=self.username)
        self.name_entry.grid(row=1, column=1, columnspan=2, pady=10)
        self.name_entry.focus_set()

        self.play = ttk.Button(self.main, text='Play Game', width=10,
                               command=self.play_game)
        self.play.grid(row=2, column=0, pady=20)

        self.quit = ttk.Button(self.main, text='Quit Game', width=10,
                               command=self.master.destroy)
        self.quit.grid(row=2, column=2, pady=20)

    def play_game(self):
        if self.username.get():
            self.main.destroy()
            self.draw_frames()
            # 헤더 프레임 구현
            self.draw_header_frame()

        else:
            messagebox.showwarning('가위 바위 보', '사용자 이름을 입력하세요!')
            self.name_entry.focus_set()

    def draw_frames(self):
        self.header = tk.Frame(self, width=400, height=100)
        self.body = tk.Frame(self, width=400, height=170, bg='blue')
        self.footer = tk.Frame(self, width=400, height=30, bg='green' )

        self.header.grid(row=0, column=0)
        self.body.grid(row=1, column=0)
        self.footer.grid(row=2, column=0)

        self.header.propagate(False)
        self.body.propagate(False)
        self.footer.propagate(False)

    def draw_header_frame(self):
        self.title = tk.Label(self.header, text='가위 바위 보', fg='black',
                              font='Verdana 14')
        self.title.grid(row=0, column=1, columnspan=3, pady=(5,7))

        self.left = tk.LabelFrame(self.header, width=150, height=55, borderwidth=5)
        self.left.grid(row=1, column=0, columnspan=2, padx=(25,10))
        self.left.grid_propagate(False)

        self.vs = tk.Label(self.header, text='Vs', fg='red', font='Verdana 15 bold')
        self.vs.grid(row=1, column=2)

        self.right = tk.LabelFrame(self.header, width=150, height=55, borderwidth=5)
        self.right.grid(row=1, column=3, columnspan=2, padx=10)
        self.right.grid_propagate(False)

        # 사용자명
        self.username = tk.Label(self.left, text=f'{self.username.get()}', fg='dodgerblue3',
                                 font='verdana 10', padx=30)
        self.username.grid(row=0, column=0, sticky='news')

        # 포인트
        self.upoint = tk.Label(self.left, text=f'({self.userPoint})', fg='dodgerblue3',
                               font='verdana 10')
        self.upoint.grid(row=1, column=0, sticky='news')

        # 사용자명
        self.username = tk.Label(self.right, text=f'system', fg='dodgerblue3',
                                 font='verdana 10', padx=30)
        self.username.grid(row=0, column=0, sticky='news')

        # 포인트
        self.spoint = tk.Label(self.right, text=f'({self.sysPoint})', fg='dodgerblue3',
                               font='verdana 10')
        self.spoint.grid(row=1, column=0, sticky='news')



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('400x300+420+240')
    root.title('가위 바위 보')

    rps_icon = PhotoImage(file='icons/rps.png')

    rock_small = PhotoImage(file='icons/rock_small.png')
    paper_small = PhotoImage(file='icons/paper_small.png')
    scissor_small = PhotoImage(file='icons/scissor_small.png')

    rock_large = PhotoImage(file='icons/rock_large.png')
    paper_large = PhotoImage(file='icons/paper_large.png')
    scissor_large = PhotoImage(file='icons/scissor_large.png')

    rock_list = [PhotoImage(file=f'animate/rock_large{i}.png') for i in range(11)]
    paper_list = [PhotoImage(file=f'animate/paper_large{i}.png') for i in range(11)]
    scissor_list = [PhotoImage(file=f'animate/scissor_large{i}.png') for i in range(11)]

    app = Application(master=root)
    app.mainloop()