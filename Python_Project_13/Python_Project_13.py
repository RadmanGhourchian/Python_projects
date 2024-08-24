from tkinter import *
import tkinter.ttk as ttk
from module import *
import tkinter.messagebox as msg
import pickle

list_tuple = []
list_tuple_2 = []

def leave(event):
    event.widget.config(bg="white", fg="black")

def buity(event):
    event.widget.config(bg='lightblue')

def saver():
    if (product_validator(product.get()) and person_validator(person.get())) == True:
        info_tuple = [product.get(), price.get(), count.get(), person.get(), In_Out.get()]
        adad = 0
        if len(list_tuple) < 1:
            if In_Out.get() == "In":
                list_tuple.append(info_tuple)

            elif In_Out.get() == "Out":
                msg.showerror("Error", "No we don't have that product!")
        else:
            for i in list_tuple:
                if product.get() != i[0]:
                    continue
                else:
                    adad = adad + 1
                    j = i
                    break

            if adad == 0:
                if In_Out.get() == "In":
                    list_tuple.append(info_tuple)
                elif In_Out.get() == "Out":
                    msg.showerror("Error", "No we don't have that product!")
            elif adad == 1:
                for i in list_tuple:
                    if i == j:
                        if In_Out.get() == "In":
                            i[2] = int(i[2]) + int(count.get())
                        elif In_Out.get() == "Out":
                            if int(i[2]) < int(count.get()):
                                msg.showerror("Error", "We don't have this many products!")
                            else:
                                i[2] = int(i[2]) - int(count.get())
                        else:
                            msg.showerror("Error", "We don't have this product!")



        refresh()
        # print(list_tuple)
        # print(count.get())
        # print(price.get())
        # if len(list_tuple) >= 1 and In_Out.get() != "Out":
        msg.showinfo("Saved", f"Dict {info_tuple} Saved !")

    else:
        msg.showerror("Error", "Please enter correct data!")


def refresh():
    for i in table.get_children():
        table.delete(i)


    for i in list_tuple:# []
        # if i[0] == product.get():
            # if In_Out.get() == "In":
        table.insert("", END, values=i, tags=i[4])





win = Tk()
win.geometry('700x500')
win.resizable(False, False)
win.title('Python Project 13')

Label(win, text='Product Name : ').place(x=20, y=15)
product = StringVar()
Entry(win, textvariable=product, width=23).place(x=125, y=15)

Label(win, text='Price : ').place(x=20, y=60)
price = StringVar()
Entry(win, textvariable=price, width=23).place(x=125, y=60)

Label(win, text='Count : ').place(x=20, y=105)
count = StringVar()
Entry(win, textvariable=count, width=23).place(x=125, y=105)

Label(win, text='Person : ').place(x=20, y=150)
person = StringVar()
Entry(win, textvariable=person, width=23).place(x=125, y=150)

Label(win, text='In or Out : ')
In_Out = StringVar()
ttk.Combobox(win, state="readonly", values=["In", "Out"], textvariable=In_Out).place(x=125, y=200)

table = ttk.Treeview(win, height=20, columns=(1, 2, 3), show="headings")
table.insert("", END, values=list_tuple)

table.heading(1, text="Product")
table.heading(2, text="Price")
table.heading(3, text="Count")

table.column(1, width=120)
table.column(2, width=120)
table.column(3, width=120)

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
