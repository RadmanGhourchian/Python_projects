import tkinter as tk

win = tk.Tk()
win.title("Python Project 12")
win.geometry("500x500")
win.resizable(False, False)

tk.Label(win, text="Python Project 12", fg="light green", font="Arail").place(x=100, y=130)

win.mainloop()