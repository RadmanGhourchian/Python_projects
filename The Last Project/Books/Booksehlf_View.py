from tkinter import *
from EntryWithLabel_Class import *
from tkinter import ttk
from Controller import BookController
import tkinter.messagebox as msg

# class BookShelfView:
#     def __init__(self):
        # self.win = Tk()
        # self.win.title("Bookshelf View")
        # self.win.geometry("500x500")
        # self.win.resizable(False, False)
        #
        #
        # self.name = EntryWithLabel(self.win, "Book's name : ", 10, 5, 130, "str")
        # self.b_id = EntryWithLabel(self.win, "Book's Id : ", 10, 45, 130, "str")
        # self.person_name = EntryWithLabel(self.win, "Person's name : ", 10, 85, 130, "str")
        # self.lang = EntryWithLabel(self.win, "Language : ", 10, 125, 130, "str")
        # Label(self.win, text="Genre : ").place(x=10, y=165)
        # self.genre = StringVar()
        # ttk.Combobox(self.win, values=["Action", "Comedy", "Novel", "Science Fiction", "Mystery", "Love Story", "Horror", "Crime", "Thriller"], state="readonly", width=17, textvariable=self.genre).place(x=140, y=165)
        # Label(self.win, text="In or Out a Book : ").place(x=10, y=205)
        # self.In_Out_Book = StringVar()
        # ttk.Combobox(self.win, values=["In", "Out"], width=17, state="readonly", textvariable=self.In_Out_Book).place(x=140, y=205)
        #
        #
        #
        # self.win.mainloop()

        # table = ttk.Treeview(self.win, columns=(1,2,3,4,5,6), height=20, show="headings")
        #
        # table.heading(1, text="Book name")
        # table.heading(2, text="Book id")
        # table.heading(3, text="Person name")
        # table.heading(4, text="Genre")
        # table.heading(5, text="Language")
        # table.heading(6, text="In or Out Book")
        #
        # table.column(1, width=120)
        # table.column(2, width=120)
        # table.column(3, width=120)
        # table.column(4, width=120)
        # table.column(5, width=120)
        # table.column(6, width=120)

        # table.place(x=100,y=100)
# def BooksehlfView():
#     # def __init__(self):
#     win = Tk()
#     win.title("Booksehlf View")
#     win.resizable(False, False)
#     win.geometry("1000x800")
#
#     table = ttk.Treeview(win, height=20, columns=(1, 2, 3, 4, 5,6), show="headings")
#
#     table.heading(1, text="ID")
#     table.heading(2, text="Name")
#     table.heading(3, text="Family")
#     table.heading(4, text="Nation_Id")
#     table.heading(5, text="username")
#     table.heading(6, text="password")
#
#     table.column(1, width=100)
#     table.column(2, width=100)
#     table.column(3, width=100)
#     table.column(4, width=100)
#     table.column(5, width=100)
#     table.column(6, width=100)
#
#     table.place(x=290, y=10)
#
#
#
#
#     name = EntryWithLabel(win, "Book's name : ", 10, 5, 130, "str")
#     b_id = EntryWithLabel(win, "Book's Id : ", 10, 45, 130, "str")
#     person_name = EntryWithLabel(win, "Person's name : ", 10, 85, 130, "str")
#     lang = EntryWithLabel(win, "Language : ", 10, 125, 130, "str")
#     Label(win, text="Genre : ").place(x=10, y=165)
#     genre = StringVar()
#     ttk.Combobox(win, values=["Action", "Comedy", "Novel", "Science Fiction", "Mystery", "Love Story", "Horror", "Crime", "Thriller"], state="readonly", width=17, textvariable=genre).place(x=140, y=165)
#     Label(win, text="In or Out a Book : ").place(x=10, y=205)
#     In_Out_Book = StringVar()
#     ttk.Combobox(win, values=["In", "Out"], width=17, state="readonly", textvariable=In_Out_Book).place(x=140, y=205)
#
#     def refresh_table():
#         for i in table.get_children():
#             table.delete(i)
#
#         for i in BookController().find_all():
#             table.insert("", END, values=i)
#
#     refresh_table()
#
#     def refresh_table_2():
#         for i in table.get_children():
#             table.delete(i)
#         status, person = BookController().save(name.get(), b_id.get(), person_name.get(), lang.get(), genre.get(),
#                                                In_Out_Book.get())
#         if status == False:
#             msg.showerror("Error", "Wrong Data!")
#         for i in BookController().find_all():
#             table.insert("", END, values=i)
#
#     Button(win, text="Save", command=refresh_table_2).place(x=290, y=300)
#
#     win.mainloop()
#
#
#
#
#
#
#     table = ttk.Treeview(win, height=20, columns=6, show="headings")
#
#     table.heading(1, text="a")
#     table.heading(2, text="b")
#     table.heading(3, text="c")
#     table.heading(4, text="d")
#     table.heading(5, text="e")
#     table.heading(6, text="f")
#
#     table.column(1, width=120)
#     table.column(2, width=120)
#     table.column(3, width=120)
#     table.column(4, width=120)
#     table.column(5, width=120)
#     table.column(6, width=120)
#
#     table.place(x=300, y=300)
#
#
#
# a = BooksehlfView()