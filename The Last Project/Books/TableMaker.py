from tkinter import *
import tkinter.ttk as ttk

class TableMaker:
    def __init__(self, win, height, cloumns, width, x, y, *args):
        table = ttk.Treeview(win, height=height, columns=cloumns, show="headings")

        for i in range(height):
            table.heading(i, text=args)

        for i in range(cloumns):
            table.column(i, width=width)

        table.place(x=x, y=y)