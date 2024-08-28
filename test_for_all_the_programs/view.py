from tkinter import *
import tkinter.ttk as ttk
from validator import *
import tkinter.messagebox as msg
from product import *
from person import *
from sell import *
import database

list_tuple = []
list_tuple_2 = []

def leave(event):
    event.widget.config(bg="white", fg="black")

def buity(event):
    event.widget.config(bg='lightblue')

def saver():
    if (product_validator(product.get()) and person_validator(brand.get())) == True:
        product1 = Product(0, product.get(), brand.get(), quintity.get(), price.get())
        product1.save()
        refresh()
        msg.showinfo("Saved", f"Saved !")

    else:
        msg.showerror("Error", "Please enter correct data!")


def refresh():
    for i in table.get_children():
        table.delete(i)

    for i in database.find_all():# []
        # if i[0] == product.get():
            # if In_Out.get() == "In":
        table.insert("", END, values=i, tags=i[4])





win = Tk()
win.geometry('1000x500')
win.resizable(False, False)
win.title('Python Project 13')

Label(win, text='Product Name : ').place(x=20, y=15)
product = StringVar()
Entry(win, textvariable=product, width=23).place(x=125, y=15)

Label(win, text='Price : ').place(x=20, y=60)
price = StringVar()
Entry(win, textvariable=price, width=23).place(x=125, y=60)

Label(win, text='quintity : ').place(x=20, y=105)
quintity = StringVar()
Entry(win, textvariable=quintity, width=23).place(x=125, y=105)

Label(win, text='Brand : ').place(x=20, y=150)
brand = StringVar()
Entry(win, textvariable=brand, width=23).place(x=125, y=150)

Label(win, text='In or Out : ')
In_Out = StringVar()
ttk.Combobox(win, state="readonly", values=["In", "Out"], textvariable=In_Out).place(x=125, y=200)

table = ttk.Treeview(win, height=20, columns=(1, 2, 3, 4, 5), show="headings")
table.insert("", END, values=list_tuple)

table.heading(1, text="ID")
table.heading(2, text="Name")
table.heading(3, text="Brand")
table.heading(4, text="Quintity")
table.heading(5, text="Price")

table.column(1, width=120)
table.column(2, width=120)
table.column(3, width=120)
table.column(4, width=120)
table.column(5, width=120)

table.tag_configure("In", foreground="green")
# table.tag_configure("Out", foreground="pink")

table.place(x=300, y=20)

refresh()

btn = Button(win, text="Save", command=saver)
btn.place(x=20, y=230)
btn.bind("<Button-1>", buity)
btn.bind("<Enter>", buity)
btn.bind("<Leave>", leave)
# button = ttk.Button(win, text="Get", command=save_button)
# button.place(x=20, y=230)

refresh()

win.mainloop()
