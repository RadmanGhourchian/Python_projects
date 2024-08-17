from tkinter import *
from tkinter.ttk import Combobox

def change(event):
    win.config(bg=color.get())

win = Tk()
win.title("Python Project 12")
win.geometry("500x500")
win.resizable(False, False)

color = StringVar()
combobox = Combobox(win,state="readonly", values=["blue", "red", "gray"], textvariable=color)
combobox.place(x=50, y=130)
combobox.current(0)
combobox.bind("<<ComboboxSelected>>", change)

win.mainloop()