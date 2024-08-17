import tkinter
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from module import *

mobile_list = []
mobile_tuple_list = []

win = tkinter.Tk()
win.title("Mobile Sail")
win.geometry('820x500')
win.resizable(False, False)

def sell():
    if model(Model.get()):
        dicttionary = {"Brand": brand.get(), "Model": Model.get(), "color": color.get(), "glass_option": glass_option.get(), "memory_option": memory_option.get(), "price":price.get()}
        tuple_list = (brand.get(), Model.get(), color.get(), glass_option.get(), memory_option.get(), price.get())
        mobile_tuple_list.append(tuple_list)
        mobile_list.append(dicttionary)
        msg.showinfo("Saved", f"Dict {dicttionary} Saved")
        rester()
        table_rester()
    else:
        msg.showerror("Error", "Please enter a validable model")

def rester():
    brand = ""
    Model = ""
    color = ""
    price = ""
    glass_option = False
    memory_option = False

def table_rester():
    for i in table.get_children():
        table.delete(i)

    for i in mobile_tuple_list:
        table.insert("", END, values=i, tags=i[2])

tkinter.Label(win, text="Brand : ").place(x=80, y=30)
brand = tkinter.StringVar()
tkinter.ttk.Combobox(win, textvariable=brand, values=("Apple", "Samsung", "Nokia"), state="readonly").place(x=140, y=30)

Model = tkinter.StringVar()
tkinter.Label(win, text="Model : ").place(x=80, y=70)
tkinter.Entry(win, textvariable=Model, width=23).place(x=140, y=70)

tkinter.Label(win, text="Color : ").place(x=80, y=110)
color = tkinter.StringVar()
tkinter.ttk.Combobox(win, textvariable=color, values=("White", "Black", "Red", "Blue", "Gray"), state="readonly").place(x=140, y=110)

tkinter.Label(win, text="Option : ").place(x=80, y=150)
glass_option = tkinter.BooleanVar()
tkinter.Checkbutton(win, text="glass option", variable=glass_option).place(x=140, y=170)

memory_option = tkinter.BooleanVar()
tkinter.Checkbutton(win, text="memory option", variable=memory_option).place(x=140, y=200)

Label(win, text="Price : ").place(x=80, y=250)
price = tkinter.StringVar()
tkinter.Entry(win, textvariable=price, width=23).place(x=140, y=250)

tkinter.Button(win, text="Sell", width=10, command=sell).place(x=90, y=330)

table =  ttk.Treeview(win, columns=(1, 2, 3, 4, 5, 6), height=12, show="headings")
table.heading(1, text="Brand")
table.heading(2, text="Model")
table.heading(3, text="Color")
table.heading(4, text="Glass option")
table.heading(5, text="Memory option")
table.heading(6, text="Price")

table.column(1, width=80)
table.column(2, width=80)
table.column(3, width=80)
table.column(4, width=80)
table.column(5, width=100)
table.column(6, width=80)

table.tag_configure("White", background="white")
table.tag_configure("Black", background="gray44")
table.tag_configure("Red", background="red")
table.tag_configure("Blue", background="navajo white")
table.tag_configure("Gray", background="gray")

table.place(x=300, y=30)

win.mainloop()