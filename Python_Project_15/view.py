from tkinter import *
import tkinter.ttk as ttk
from validator import *
import tkinter.messagebox as msg
from product import *
from person import *
from sell import *
import database
import database_2

list_tuple = []
list_tuple_2 = []

def leave(event):
    event.widget.config(bg="white", fg="black")

def buity(event):
    event.widget.config(bg='lightblue')

def saver():
    product1 = Product(0, product.get(), brand.get(), quintity.get(), price.get(), person.get())
    product1.save()
    refresh()
    msg.showinfo("Saved", f"Saved !")

def edit_click():
    product1 = Product(id.get(), product.get(), brand.get(), quintity.get(), price.get(), person.get())
    product1.edit()
    refresh()
    msg.showinfo("Edited", f"Edited !")

def delete_click():
    if msg.askyesno("Delete", "Are you sure you want to delete this product?"):
        product1 = Product(id.get(), None, None, None, None, None)
        product1.delete()
        msg.showinfo("Deleted", f"Deleted !")
        refresh()

def sell_click():
    sell = Sell(id.get(), person.get(), brand.get(), quintity.get(), price.get())
    sell.sell()
    msg.showinfo("Sold", f"Sold !")
def refresh():
    for i in table.get_children():
        table.delete(i)

    for i in database.find_all():
        table.insert("", END, values=i, tags=i[4])

def person_save():
    person1 = Person(id.get(), name.get(), family.get(), nation_id.get(), username.get(), password.get())
    person1.save()
    person_refresh()
    msg.showinfo("Saved", f"Saved !")
def person_edit():
    person1 = Person(id.get(), name.get(), family.get(), nation_id.get(), username.get(), password.get())
    person1.edit()
    person_refresh()
    msg.showinfo("Edited", f"Edited !")
def person_delete():
    if msg.askyesno("Delete", "Are you sure you want to delete this person?"):
        person1 = Person(id.get(), name.get(), family.get(), nation_id.get(), username.get(), password.get())
        person1.delete()
        person_refresh()
        msg.showinfo("Deleted", f"Deleted !")

def person_refresh():
    for i in table_person.get_children():
        table_person.delete(i)

    for i in database_2.find_all():
        table_person.insert("", END, values=i)



win = Tk()
win.geometry('1760x550')
# win.resizable(False, False)
win.title('Python Project 15')

Label(win, text="Id : ").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id).place(x=125, y=20)

Label(win, text='Product Name : ').place(x=20, y=50)
product = StringVar()
Entry(win, textvariable=product, width=23).place(x=125, y=50)

Label(win, text='Price : ').place(x=20, y=80)
price = StringVar()
Entry(win, textvariable=price, width=23).place(x=125, y=80)

Label(win, text='quintity : ').place(x=20, y=110)
quintity = StringVar()
Entry(win, textvariable=quintity, width=23).place(x=125, y=110)

Label(win, text='Brand : ').place(x=20, y=140)
brand = StringVar()
Entry(win, textvariable=brand, width=23).place(x=125, y=140)

# Label(win, text='In or Out : ').place(x=20, y=190)
# In_Out = StringVar()
# ttk.Combobox(win, state="readonly", values=["In", "Out"], textvariable=In_Out).place(x=125, y=190)

Label(win, text="Person : ").place(x=20, y=170)
person = StringVar()
Entry(win, textvariable=person, width=23).place(x=125, y=170)

Label(win, text='Name : ').place(x=20, y=200)
name = StringVar()
Entry(win, textvariable=name, width=23).place(x=125, y=200)

Label(win, text='Family : ').place(x=20, y=230)
family = StringVar()
Entry(win, textvariable=family, width=23).place(x=125, y=230)

Label(win, text='National ID : ').place(x=20, y=260)
nation_id = StringVar()
Entry(win, textvariable=nation_id, width=23).place(x=125, y=260)

Label(win, text="Username : ").place(x=20, y=290)
username = StringVar()
Entry(win, textvariable=username, width=23).place(x=125, y=290)

Label(win, text='Password : ').place(x=20, y=320)
password = StringVar()
Entry(win, textvariable=password, width=23).place(x=125, y=320)

table = ttk.Treeview(win, height=20, columns=(1, 2, 3, 4, 5,6), show="headings")
table.insert("", END, values=list_tuple)

table.heading(1, text="ID")
table.heading(2, text="Name")
table.heading(3, text="Brand")
table.heading(4, text="Quintity")
table.heading(5, text="Price")
table.heading(6, text="Person")

table.column(1, width=120)
table.column(2, width=120)
table.column(3, width=120)
table.column(4, width=120)
table.column(5, width=120)
table.column(6, width=120)

table.tag_configure("In", foreground="green")
# table.tag_configure("Out", foreground="pink")

table.place(x=300, y=20)

table_person = ttk.Treeview(win, height=20, columns=(1, 2, 3, 4, 5,6), show="headings")
table_person.insert("", END, values=list_tuple)

table_person.heading(1, text="ID")
table_person.heading(2, text="Name")
table_person.heading(3, text="Family")
table_person.heading(4, text="Nation_Id")
table_person.heading(5, text="username")
table_person.heading(6, text="password")

table_person.column(1, width=120)
table_person.column(2, width=120)
table_person.column(3, width=120)
table_person.column(4, width=120)
table_person.column(5, width=120)
table_person.column(6, width=120)

table_person.place(x=1030, y=20)

refresh()
person_refresh()

btn_save = Button(win, text="Save", command=saver)
btn_save.place(x=20, y=370)
btn_save.bind("<Button-1>", buity)
btn_save.bind("<Enter>", buity)
btn_save.bind("<Leave>", leave)

btn_edit = Button(win, text="Edit", command=edit_click)
btn_edit.place(x=90, y=370)
btn_edit.bind("<Button-1>", buity)
btn_edit.bind("<Enter>", buity)
btn_edit.bind("<Leave>", leave)

btn_delete = Button(win, text="Delete", command=delete_click)
btn_delete.place(x=150, y=370)
btn_delete.bind("<Button-1>", buity)
btn_delete.bind("<Enter>", buity)
btn_delete.bind("<Leave>", leave)

btn_sell = Button(win, text="Sell", command=sell_click)
btn_sell.place(x=210, y=370)


btn_save_person = Button(win, text="Save Person", command=person_save)
btn_save_person.place(x=20, y=460)
btn_save_person.bind("<Button-1>", buity)
btn_save_person.bind("<Enter>", buity)
btn_save_person.bind("<Leave>", leave)

btn_edit_person = Button(win, text="Edit Person", command=person_edit)
btn_edit_person.place(x=150, y=460)
btn_edit_person.bind("<Button-1>", buity)
btn_edit_person.bind("<Enter>", buity)
btn_edit_person.bind("<Leave>", leave)

btn_delete_person = Button(win, text="Delete Person", command=person_delete)
btn_delete_person.place(x=280, y=460)
btn_delete_person.bind("<Button-1>", buity)
btn_delete_person.bind("<Enter>", buity)
btn_delete_person.bind("<Leave>", leave)
# button = ttk.Button(win, text="Get", command=save_button)
# button.place(x=20, y=230)

refresh()

win.mainloop()
