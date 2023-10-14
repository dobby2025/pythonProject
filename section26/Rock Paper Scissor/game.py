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

    def main_frame(self):
        self.main = tk.Frame(self, width=400, height=300, bg='white')
        self.main.grid(row=0, column=0)
        self.main.grid_propagate(False)

        self.game_lbl = tk.Label(self.main, image=rps_icon)
        self.game_lbl.grid(row=0, column=0, columnspan=3, padx=90, pady=10)





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