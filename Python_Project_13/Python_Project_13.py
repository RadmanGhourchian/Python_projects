from tkinter import *
import tkinter.ttk as ttk
from module import *
import tkinter.messagebox as msg

list_tuple = []
sum_list = []


def saver():
    if (product_validator(product.get()) and person_validator(person.get())) == True:
        info_tuple = [product.get(), price.get(), count.get(), person.get(), In_Out.get()]
        list_tuple.append(info_tuple)
        refresh()
        print(list_tuple)
        if len(list_tuple) >= 1 and In_Out.get() != "Out":
            msg.showinfo("Saved", f"Dict {info_tuple} Saved !")



        # if float(count.get()) < 2 and In_Out.get() == "Out":
        #     msg.showerror("Error", "There is no data to reduce it!")
        #     print("")
        #     refresh()
        # else:
        #     for i in list_tuple:
        #         if i[0] == product.get():
        #             msg.showinfo("Saved", f"Dict {info_tuple} Saved !")
        #             return None

        #     list_tuple.append(info_tuple)
        #     refresh()
        #     print(list_tuple)
        #     msg.showinfo("Saved", f"Dict {info_tuple} Saved !")
    else:
        msg.showerror("Error", "Please enter correct data!")



def adder():
    add = 0
    for i in list_tuple:
        if product.get() == i[0]:
            add = add + 1

    for i in list_tuple:
        if add == 1:
            table.insert("", END, values=i)
        elif add > 1:
            if i[0] == product.get():
                if In_Out.get() == "In":
                    a = i
                    a2 = [a[0], a[1], a[2], a[3], a[4]]
                    list_tuple.append(a2)
                    table.delete(i)
                    a[2] = str(int(a[2]) + int(count.get()))
                    table.insert("", END, values=a2)
                    return None


def refresh():
    for i in table.get_children():
        table.delete(i)

    for i in list_tuple:
        if i[0] == product.get():
            if In_Out.get() == "In":
                # table.insert("", END, values=i)
                adder()
            elif In_Out.get() == "Out" and len(list_tuple) <=1:
                list_tuple.clear()
                msg.showerror("error", "aaaa")
            elif int(i[2]) < int(count.get()):
                list_tuple.remove(i)
                msg.showerror("Error", "You don't you that much data")
            elif int(i[2]) > int(count.get()):
                i[2] = int(i[2]) - int(count.get())
                if i[2] == 0:
                    list_tuple.remove(i)
                    return None
        else:
            msg.showerror("Error", "aaaaaaa")




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

table.tag_configure("In", foreground="lightgreen")
# table.tag_configure("Out", foreground="pink")

table.place(x=300, y=20)

refresh()

Button(win, text="Save", command=saver).place(x=20, y=230)
# button = ttk.Button(win, text="Get", command=save_button)
# button.place(x=20, y=230)

refresh()

win.mainloop()
