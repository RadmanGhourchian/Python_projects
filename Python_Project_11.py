import tkinter
import tkinter.ttk as ttk
from module import *
import tkinter.messagebox as msg

mobile_list = []

win = tkinter.Tk()
win.title("Mobile Sail")
win.geometry('500x500')

def sell():
    if model(Model.get()):
        dicttionary = {"Brand": brand.get(), "Model": Model.get(), "color": color.get(), "glass_option": glass_option.get(), "memory_option": memory_option.get()}
        mobile_list.append(dicttionary)
        msg.showinfo("Saved", f"Dict {dicttionary} Saved")
        rester()
    else:
        msg.showerror("Error", "Please enter a validable model")

def rester():
    brand = ""
    Model = ""
    color = ""
    glass_option = False
    memory_option = False

tkinter.Label(win, text="Brand : ").place(x=80, y=30)
brand = tkinter.StringVar()
tkinter.ttk.Combobox(win, textvariable=brand, values=("Apple", "Samsung", "Nokia"), state="readonly").place(x=140, y=30)

Model = tkinter.StringVar()
tkinter.Label(win, text="Model : ").place(x=80, y=70)
tkinter.Entry(win, textvariable=Model, width=23).place(x=140, y=70)

tkinter.Label(win, text="Color : ").place(x=80, y=110)
color = tkinter.StringVar()
tkinter.ttk.Combobox(win, textvariable=color, values=("White", "Black", "Red", "Blue"), state="readonly").place(x=140, y=110)

tkinter.Label(win, text="Option : ").place(x=80, y=150)
glass_option = tkinter.BooleanVar()
tkinter.Checkbutton(win, text="glass option", variable=glass_option).place(x=140, y=170)

memory_option = tkinter.BooleanVar()
tkinter.Checkbutton(win, text="memory option", variable=memory_option).place(x=140, y=200)

tkinter.Button(win, text="Sell", width=10, command=sell).place(x=90, y=250)

win.mainloop()